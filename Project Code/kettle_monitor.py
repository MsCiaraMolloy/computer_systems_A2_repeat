#Kettle monitor script - runs on the Raspberry Pi.
#Uses the SenseHat temperature sensor to detect when the kettle is turned on.
#When a boil is detected it sends the time and temperature to ThingSpeak via HTTP.
#This script is the data collection component of my Green Genie project.

from sense_hat import SenseHat
from datetime import datetime
import requests
import time

sense = SenseHat()

#My ThingSpeak channel details.
write_api_key = "OIR2H7GT2UNWCUXI"
thingspeak_url = "https://api.thingspeak.com/update"

#Temperature threshold - the temp the sensehat needs to reach before a boil is logged.
#Set lower for testing at room temp, raise to ~40 when placed near the kettle.
temp_threshold = 40

#Cooldown period in seconds between detections.
#Stops one boil being logged multiple times while the temp stays high.
cooldown = 300

#Tracking the time of the last detected boil.
last_boil_time = 0

print("Green Genie kettle monitor is running...")

while True:
    #Reading the current temperature from the SenseHat sensor.
    current_temp = sense.get_temperature()
    current_time = time.time()

    #Checking if temp is above threshold and enough time has passed since last boil.
    if current_temp > temp_threshold and (current_time - last_boil_time) > cooldown:

        #Recording the time of the boil in HH.MM format to match my csv format.
        boil_time = datetime.now().strftime("%H.%M")
        print(f"Boil detected at {boil_time}, temperature: {current_temp:.1f}C")

        #Sending the boil time and temperature to ThingSpeak via HTTP POST.
        #field1 = boil time, field2 = temperature at time of boil.
        payload = {
            "api_key": write_api_key,
            "field1":  boil_time,
            "field2":  round(current_temp, 2)
        }

        #Posting to ThingSpeak and checking the response.
        #ThingSpeak returns 0 if the post failed, or the entry id if successful.
        try:
            response = requests.post(thingspeak_url, data=payload)
            if response.text == "0":
                print("ThingSpeak post failed - check api key or channel settings.")
            else:
                print(f"Logged to ThingSpeak successfully. Entry id: {response.text}")
        except Exception as e:
            print(f"Could not connect to ThingSpeak: {e}")

        #Updating last boil time so the cooldown resets.
        last_boil_time = current_time

    #Waiting 5 seconds before taking the next reading.
    time.sleep(5)
