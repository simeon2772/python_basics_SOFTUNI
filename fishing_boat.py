budget = int(input())
season = input()
count_fishermen = int(input())
rent_ship = 0
if season == "Spring":
    rent_ship = 3000
    if count_fishermen <= 6:
        rent_ship = rent_ship * 0.90
    elif 7 < count_fishermen <= 11:
        rent_ship = rent_ship * 0.85
    else:
        rent_ship = rent_ship * 0.75
elif season == "Summer" or season == "Autumn":
    rent_ship = 4200
    if count_fishermen <= 6:
        rent_ship = rent_ship * 0.90
    elif 7 < count_fishermen <= 11:
        rent_ship = rent_ship * 0.85
    else:
        rent_ship = rent_ship * 0.75
elif season == "Winter":
    rent_ship = 2600
    if count_fishermen <= 6:
        rent_ship = rent_ship * 0.90
    elif 7 < count_fishermen <= 11:
        rent_ship = rent_ship * 0.85
    else:
        rent_ship = rent_ship * 0.75

if count_fishermen % 2 == 0 and season != "Autumn":
    rent_ship = rent_ship * 0.95

diff = abs(budget - rent_ship)

if budget >= rent_ship:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")





