film_budget = float(input())
actors = int(input())
price_clothing_per_actor = float(input())
decor_amount = film_budget * 0.10
clothing_amount = actors * price_clothing_per_actor
if actors > 150:
    clothing_amount = clothing_amount * 0.90
expenses = decor_amount + clothing_amount

diff = abs(expenses - film_budget)
if expenses <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
