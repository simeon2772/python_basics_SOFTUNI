dancers = int(input())
points = float(input())
season = input()
place = input()
price = 0
if place == "Bulgaria":
    price = points * dancers
    if season == "summer":
        price *= 0.95
    elif season == "winter":
        price *= 0.92
elif place == "Abroad":
    price = dancers * points
    price = price + (price / 2)
    if season == "summer":
        price *= 0.90
    elif season == "winter":
        price *= 0.85

charity = price * 0.75

money_left = price - charity
money_per_dancer = money_left / dancers

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")