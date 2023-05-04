cat_count = int(input())
small_cats = 0
big_cats = 0
large_cats = 0
total_cats_food_grams = 0
one_kg_price = 12.45
for cats in range(1, cat_count + 1):
    grams_per_cat = float(input())
    if 100 <= grams_per_cat < 200:
        small_cats += 1
        total_cats_food_grams += grams_per_cat
    elif 200 <= grams_per_cat < 300:
        big_cats += 1
        total_cats_food_grams += grams_per_cat
    elif 300 <= grams_per_cat < 400:
        large_cats += 1
        total_cats_food_grams += grams_per_cat
total_cats_food_kg = total_cats_food_grams / 1000
price_cat_food_per_day = total_cats_food_kg * one_kg_price

print(f"Group 1: {small_cats} cats.")
print(f"Group 2: {big_cats} cats.")
print(f"Group 3: {large_cats} cats.")
print(f"Price for food per day: {price_cat_food_per_day:.2f} lv.")