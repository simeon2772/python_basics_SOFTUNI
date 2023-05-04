budget = float(input())
season = input()
destination = ""
kind_of_holiday = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        kind_of_holiday = "Camp"
        budget = budget * 0.30
    elif season == "winter":
        kind_of_holiday = "Hotel"
        budget = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        kind_of_holiday = "Camp"
        budget = budget * 0.40
    elif season == "winter":
        kind_of_holiday = "Hotel"
        budget = budget * 0.80
else:
    destination = "Europe"
    budget = budget * 0.90
    if season == "summer" or season == "winter":
        kind_of_holiday = "Hotel"

print(f"Somewhere in {destination}")
print(f"{kind_of_holiday} - {budget:.2f}")







