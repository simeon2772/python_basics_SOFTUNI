month = input()
night = int(input())
apartment = 0
studio = 0
studio_price_per_night = 0
apartment_price_per_night = 0
if month == "May" or month == "October":
    studio_price_per_night = 50
    if 7 < night < 14:
        studio = (studio_price_per_night * 0.95) * night
    elif 14 < night:
        studio = (studio_price_per_night * 0.70) * night
    else:
        studio = studio_price_per_night * night
    apartment_price_per_night = 65
    if 14 < night:
        apartment = (apartment_price_per_night * 0.90) * night
    else:
        apartment = apartment_price_per_night * night
elif month == "June" or month == "September":
    studio_price_per_night = 75.20
    if 14 < night:
        studio = (studio_price_per_night * 0.80) * night
    else:
        studio = studio_price_per_night * night
    apartment_price_per_night = 68.70
    if 14 < night:
        apartment = (apartment_price_per_night * 0.90) * night
    else:
        apartment = apartment_price_per_night * night
elif month == "July" or month == "August":
    studio_price_per_night = 76
    studio = studio_price_per_night * night
    apartment_price_per_night = 77
    if 14 < night:
        apartment = (apartment_price_per_night * 0.90) * night
    else:
        apartment = apartment_price_per_night * night

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")








