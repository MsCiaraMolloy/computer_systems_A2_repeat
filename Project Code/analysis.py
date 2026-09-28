#Importing supplier data from electricity_rates.py so we can compare costs across all providers.
from electricity_rates import suppliers, pso_levy, current_supplier_name, current_day_rate, current_night_rate, current_peak_rate, current_asc

#Updated: importing requests library to fetch data from ThingSpeak via HTTP.
import requests

#Creating a sample csv to simulate one weeks records.
#cycle_times = open("sample.csv","w")
#cycle_times.write("00.00,12.30,17.32,18.05,06.09,08.12,09.10,07.15,12.05,20.08,22.00,15.20,14.00,17.10,19.25")
#cycle_times.close()

#Updated: added ThingSpeak channel details to fetch live boil data via the REST API.
#My channel id and read api key are stored here - update these with your own channel details.
#Results=200 fetches the last 200 entries from the channel, adjust as needed.
channel_id = "3512900"
read_api_key = "IXUBWCWPX6Q3VLG9"
thingspeak_url = f"https://api.thingspeak.com/channels/{channel_id}/fields/1.json?api_key={read_api_key}&results=200"

#Updated: fetching boil time data from ThingSpeak instead of reading a local csv file.
#The response comes back as JSON - pulling out the field1 values which are the boil times.
#If the request fails it falls back to the local sample.csv so the script still runs.
response = requests.get(thingspeak_url)

if response.status_code == 200:
    data = response.json()
    raw_times = [entry["field1"] for entry in data["feeds"] if entry["field1"] is not None]
    print(f"Fetched {len(raw_times)} boil records from ThingSpeak.")
else:
    print(f"Could not reach ThingSpeak (status {response.status_code}), falling back to sample.csv.")
    boil_times = open("sample.csv","r")
    raw_times = boil_times.read().split(",")
    boil_times.close()

#Converting items in the list to floats - same as before, works for both ThingSpeak and csv data.
all_times = [float(item) for item in raw_times]

#Calculating total number of times the kettle was boiled.
total_boils = len(all_times)
print(f"The kettle was boiled {total_boils} times over this 7 day period.")

#Organising the list in ascending order
all_times.sort()
print(all_times)

#Counting number of peak/day/night boils throughout the week
day_boils = 0
night_boils = 0
peak_boils = 0

for item in all_times:
    if item >= 17.0 and item <= 19.0:
        peak_boils +=1
    elif item <8.0 or item >23.0:
        night_boils +=1
    else:
        day_boils +=1

print(f"Peak hours kettle boils: {peak_boils} \nNightime hours kettle boils: {night_boils} \nDaytime hours kettle boils: {day_boils}")


#Calculate total kilowatt hours used
#Formula: watts x hours / 1000 = kWh
#My Kettle boils for 3mins 40 sec at 3000w see video of experiment for this.
single_boil_kWh = (3000*0.06) / 1000
total_kw = round(total_boils*single_boil_kWh,2)
print(f"The total kWh used by the kettle during this period was {total_kw} kWh.")

#Calculate the cost of total energy used day/night/peak/total.
# Updated: Replaced hardcoded rate values with the imported current supplier rates from electricity_rates.py.
# This means if you update your rates in electricity_rates.py, this file picks them up automatically.
my_peak_rate = current_peak_rate
my_day_rate  = current_day_rate
my_night_rate = current_night_rate

peak_cost = round((single_boil_kWh*peak_boils)*my_peak_rate,2)
print(f"The peak cost was €{peak_cost}.")

day_cost = round((single_boil_kWh*day_boils)*my_day_rate,2)
print(f"The day cost was €{day_cost}.")

night_cost = round((single_boil_kWh*night_boils)*my_night_rate,2)
print(f"The night cost was €{night_cost}.")

total_cost = night_cost+day_cost+peak_cost
print(f"The total cost of running the kettle during this timeframe was €{total_cost}.")



# Updated: Supplier comparison section - new addition.
# Loops through all suppliers in electricity_rates.py, calculates what
# this week's kettle usage would have cost with each one, then sorts
# cheapest first and compares against the current supplier's actual cost.
# Weekly ASC is included to give a realistic total bill.


print("\n--- Supplier Comparison (based on this week's kettle usage) ---")

# Calculate the current supplier's weekly cost (unit rates + weekly share of ASC + PSO levy)
weekly_asc_current = current_asc / 52
weekly_pso = pso_levy / 52
current_unit_cost = (
    (single_boil_kWh * peak_boils  * current_peak_rate) +
    (single_boil_kWh * day_boils   * current_day_rate)  +
    (single_boil_kWh * night_boils * current_night_rate)
)
current_total = round(current_unit_cost + weekly_asc_current + weekly_pso, 4)

# Build a results list - calculate the same cost for every supplier in the list
comparison_results = []
for supplier in suppliers:
    weekly_asc = supplier["asc"] / 52
    unit_cost = (
        (single_boil_kWh * peak_boils  * supplier["peak"]) +
        (single_boil_kWh * day_boils   * supplier["day"])  +
        (single_boil_kWh * night_boils * supplier["night"])
    )
    total = round(unit_cost + weekly_asc + weekly_pso, 4)
    comparison_results.append({"name": supplier["name"], "total": total})

# Sort all suppliers cheapest first
comparison_results.sort(key=lambda x: x["total"])

# Print the ranked list, flagging the current supplier where it appears
for rank, result in enumerate(comparison_results, start=1):
    if result["name"] == current_supplier_name:
        print(f"{rank}. {result['name']}: €{result['total']:.4f}  <-- your current supplier (comparison rate)")
    else:
        saving = round(current_total - result["total"], 4)
        if saving > 0:
            print(f"{rank}. {result['name']}: €{result['total']:.4f}  (saves €{saving:.4f} vs your current bill rate)")
        else:
            print(f"{rank}. {result['name']}: €{result['total']:.4f}  (more expensive than your current bill rate)")

# Updated: Final recommendation - finds the cheapest supplier overall and compares
# it to what the user is actually paying (current_total uses their real bill rates).
cheapest = comparison_results[0]
print(f"\nYou are currently paying: €{current_total:.4f}/week for kettle use (inc. ASC & PSO share).")

if cheapest["name"] == current_supplier_name:
    print("Your current supplier offers the best rate for your usage pattern - no switch needed!")
else:
    weekly_saving = round(current_total - cheapest["total"], 4)
    yearly_saving = round(weekly_saving * 52, 2)
    if weekly_saving > 0:
        print(f"Switching to {cheapest['name']} could save you €{weekly_saving:.4f}/week (approx. €{yearly_saving:.2f}/year) on kettle use alone.")
    else:
        print(f"Based on these rates, your current bill rate is already competitive. Consider reviewing your full household usage before switching.")
