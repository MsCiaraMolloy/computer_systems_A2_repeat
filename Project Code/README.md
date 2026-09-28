**** Plan & Activity Log ****
#1st Jan 2026 ****
Aims:

Set up an apparatus that measures temperature of my dryer door. 
When it reaches a certain temperature (ie. the dryer is on). 
The time of day that the dryer was used will be sent to a database of some sort.
Over the period of 7 days the time and no. of uses will be stored in a CSV file.

A. Cost
I will then clculate the cost of running the dryer at each time using day/night/peak rates.
I can then calculate if there is a cheaper option using the current rates of electricity.

B. CO2 Emmission
I will calculate the energy used in total and give an estimate 
of how many trees it would take to offset the CO2 emmission over the week.

#6th Jan 2026****

Research:

Energy Suppliers
There are only 11 electricity suppliers in Ireland available for domestic purpose.
https://www.cru.ie/consumer-information/switch-supplier/energy-suppliers-in-ireland/
They are:
1. Arden Energy
2. Bord Gais Energy
3. Pinergy
4. Community Power
5. Ecopower
6. Energia
7. Electric Ireland
8. Flogas
9. Yuno
10. SSE Airtricity
11. Water Power

Things to consider when calculating price of a cycle.
a. Annual Standard Charge of Company 
    (Divide by 52 for 7 day period)
b. Unit Rate for day/night/peak 
    Peak (5pm-7pm) is most expensive, 
    Day (8am-11pm, excluding peak) is mid-range, 
    Night (11pm-8am) is cheapest.
c. Cashback option.

Notes:
1. I will use the rates as of 1st Jan 2026, this data will be gathered from the company websites.
2. I will use the kilowatt usage of my personal dryer the data of which is in the manual.
3. Kilowatt to CO2 calculator. https://www.cencepower.com/calculators/kwh-to-co2-calculator 
4. I will calculate the C02 emmissions used for that week and I will attempt to calculate a 
    way in which a person can offset this.

** ThingSpeak Account set up and channel ready @ Green_Genie

#7th Jan 2026 ****
Begin Coding Data Collection

#8th Jan 2026
After my first few attempts at trying to attach the RPi and record the temperature of my dryer I have decided to change the appliance, to record the temperature of the kettle to signal when it is turned on and to generate energy consumption. 
The data collected will be larger as the kettle in my house is run a lot more than the dryer. I would assume the cost will be lower but this project will tell me exactly.
An extension of this project could create a way to record different appliances and send real time updates to the user on a greener more cost friendly way to use the appliance. 

Research on Kettle energy consumption
According to the below article (Durand 2022, et. al.), 
Reference:
Durand, A., Hirzel, S., Rohde, C., Gebele, M., Lopes, C., Olsson, E., & Barkhausen, R. (2022). Electric Kettles: An Assessment of Energy-Saving Potentials for Policy Making in the European Union. Sustainability, 14(20), 12963. https://doi.org/10.3390/su142012963


#9th Jan 2026

Today I am carrying out an experiment to see exactly how much electricity my kettle uses for one boil. According to the sticker at the end of my kettle the watts is 3000w. I will time how long it takes to boil a full kettle of 1.5 litres using a timer. I will also use a thermometer to check the temperature before and after boiling. I will then calculate using the watts and the appropriate formula the exact kWh.
I will also video this experiment. (See Experiment Folder)

#11th Jan 2026
I am collecting data from the kettle and storing the data to a csv file. 
I will use the data to analyse and display results.


#28 Sep 2026
Carrying on from the work in January I have created a github repo and uploaded the work done in Jan.
I will now attempt to set up the Rpi and connect to ThingSpeak.




