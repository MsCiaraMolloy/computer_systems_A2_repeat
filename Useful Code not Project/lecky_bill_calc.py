name = input("Name:")
day_rate = float(input("day rate (euro):"))
night_rate = float(input("night rate(euro):"))
peak_rate = float(input("peak rate(euro):"))

standard_charge = float(input("standard charge (euro):"))/12
'''
day_bill_kw = float(input("day kw:"))
night_bill_kw = float(input("night kw:"))
peak_bill_kw = float(input("peak kw:"))
'''
day_bill_kw = 376
night_bill_kw = 116
peak_bill_kw = 63.9
day_total = day_rate*day_bill_kw
night_total = night_rate*night_bill_kw
peak_total = peak_rate*peak_bill_kw

total = day_total+night_total+peak_total+standard_charge
print(total)
