kind_of_flower = input()
count_of_flower = int(input())
budget = int(input())
price_flowers = 0

if kind_of_flower == "Roses":
    price_flowers = 5 * count_of_flower
    if count_of_flower > 80:
        price_flowers = price_flowers * 0.90
elif kind_of_flower == "Dahlias":
    price_flowers = 3.80 * count_of_flower
    if count_of_flower > 90:
        price_flowers = price_flowers * 0.85
elif kind_of_flower == "Tulips":
    price_flowers = 2.80 * count_of_flower
    if count_of_flower >80:
        price_flowers = price_flowers * 0.85
elif kind_of_flower == "Narcissus":
    price_flowers = 3 * count_of_flower
    if count_of_flower < 120:
        price_flowers = price_flowers * 1.15
elif kind_of_flower == "Gladiolus":
    price_flowers = 2.50 * count_of_flower
    if count_of_flower < 80:
        price_flowers = price_flowers * 1.20

diff = abs(budget - price_flowers)
if price_flowers <= budget:
    print(f"Hey, you have a great garden with {count_of_flower} {kind_of_flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")