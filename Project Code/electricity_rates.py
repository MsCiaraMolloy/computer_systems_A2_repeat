# This file stores electricity supplier rate data for Ireland (rates as of Jan 2026).
# Sources: individual supplier websites.
# Arden Energy and Ecopower excluded - rates not publicly available.
#
# Updated: Refactored from separate parallel lists into a single list of dictionaries.
# This makes it easy to loop through all suppliers and calculate costs in analysis.py.
# Each dictionary contains: name, day rate, night rate, peak rate, and
# annual standing charge (asc) in euro. PSO levy is shared across all suppliers.

# PSO (Public Service Obligation) levy - same for all suppliers (euro/year)
pso_levy = 19.10

# Updated: Supplier data now stored as a list of dictionaries (one per supplier).
# Rates are in euro per kWh. asc is the annual standing charge in euro.
suppliers = [
    {"name": "Bord Gais",        "day": 0.2828, "night": 0.2828, "peak": 0.2828, "asc": 244.76},
    {"name": "Pinergy",          "day": 0.4177, "night": 0.3177, "peak": 0.4472, "asc": 283.47},
    {"name": "Community Power",  "day": 0.3308, "night": 0.1915, "peak": 0.3984, "asc": 278.50},
    {"name": "Energia",          "day": 0.2781, "night": 0.1529, "peak": 0.3122, "asc": 265.01},
    {"name": "Electric Ireland", "day": 0.2814, "night": 0.1479, "peak": 0.3002, "asc": 250.77},
    {"name": "Flogas",           "day": 0.2660, "night": 0.1346, "peak": 0.3259, "asc": 270.45},
    {"name": "Yuno",             "day": 0.3416, "night": 0.2064, "peak": 0.3416, "asc": 247.94},
    {"name": "SSE Airtricity",   "day": 0.2829, "night": 0.1818, "peak": 0.3169, "asc": 263.86},
    {"name": "Water Power",      "day": 0.3505, "night": 0.2531, "peak": 0.3798, "asc": 246.67},
]

# Updated: Current supplier details stored here separately.
# These are the actual rates on the user's bill (may differ from the comparison rates above
# due to discounts, cashback offers etc.).
# Update current_supplier_name to match your provider if you switch.
current_supplier_name = "Energia"
current_day_rate   = 0.3865
current_night_rate = 0.2125
current_peak_rate  = 0.4340
current_asc        = 265.01
