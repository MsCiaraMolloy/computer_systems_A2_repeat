#Creating a sample csv to simulate one weeks records.
cycle_times = open("sample.csv","w")
cycle_times.write("00.00,12.30,17.32,18.05,06.09,08.12,09.10,07.15,12.05,20.08,22.00,15.20,14.00,17.10,19.25")
cycle_times.close()


#Accessing csv file for analysis
boil_times = open("sample.csv","r")
all_times = boil_times.read()
boil_times.close()
print(all_times)

#Converting items in the list to floats.
all_times = all_times.split(",")
all_times = [float(item) for item in all_times]

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
my_peak_rate = 0.434
my_day_rate = 0.3865
my_night_rate = 0.2125

peak_cost = round((single_boil_kWh*peak_boils)*my_peak_rate,2)
print(f"The peak cost was €{peak_cost}.")

day_cost = round((single_boil_kWh*day_boils)*my_day_rate,2)
print(f"The day cost was €{day_cost}.")

night_cost = round((single_boil_kWh*night_boils)*my_night_rate,2)
print(f"The night cost was €{night_cost}.")

total_cost = night_cost+day_cost+peak_cost
print(f"The total cost of running the kettle during this timeframe was €{total_cost}.")