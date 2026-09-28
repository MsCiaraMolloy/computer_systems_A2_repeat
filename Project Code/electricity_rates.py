# This file creates a csv file to store the energy company data.
# 1. Arden Energy - none available
# 2. [0]Bord Gais Energy - 28.28c/kWh for day/night/peak 
# 3. [1]Pinergy - day 41.77c/kWh / night 31.77c/kwH / peak 44.72c/kWh
# 4. [2]Community Power - day 33.08c/kWh / night 19.15c/kwH / peak 39.84c/kWh
# 5. Ecopower - none available
# 6. [3]Energia - day 27.81c/kWh / night 15.29c/kwH / peak 31.22c/kWh
# 7. [4]Electric Ireland - day 28.14c/kWh / night 14.79c/kwH / peak 30.02c/kWh
# 8. [5]Flogas - day 26.6c/kWh / night 13.46c/kwH / peak 32.59c/kWh
# 9. [6]Yuno - day/peak 34.16./kwh / night 20.64c/kwh
# 10.[7]SSE Airtricity - day 28.29c/kWh / night 18.18c/kwH / peak 31.69c/kWh
# 11.[8]Water Power - day 35.05c/kWh / night 25.31c/kwH / peak 37.98c/kWh

'''lecky_rates = open("electricity_rates.csv","w")
lecky_rates.write("")
lecky_rates.close()'''

names = ['bord_gais','pinergy','community_power','energia','electric_ireland','flogas','yuno','sse_airtricity','water_power']
day_rates = [0.2828, 0.4177, 0.3308, 0.2781, 0.2814, 0.2660, 0.3416, 0.2829, 0.3505]
night_rates = [0.2828, 0.3177, 0.1915, 0.1529, 0.1479, 0.1346, 0.2064, 0.1818, 0.2531]
peak_rates = [0.2828, 0.4472, 0.3984, 0.3122, 0.3002, 0.3259, 0.3416, 0.3169, 0.3798]
asc = [244.76, 283.47, 278.50, 265.01, 250.77, 270.45, 247.94, 263.86, 246.67]
pso_levy = 19.10