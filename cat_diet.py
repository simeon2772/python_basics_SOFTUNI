fat_percentage = int(input())
protein_percentage = int(input())
carbohydrates_percentage = int(input())
total_cat_calories = int(input())
water_contend_percentage = int(input())

total_fat = (total_cat_calories * (fat_percentage / 100)) / 9
total_protein = (total_cat_calories * (protein_percentage / 100)) / 4
total_carbohydrates = (total_cat_calories * (carbohydrates_percentage / 100)) / 4

total_food = total_fat + total_protein + total_carbohydrates

calories_per_gram = total_cat_calories / total_food
calories_without_water = calories_per_gram * (water_contend_percentage / 100)
total_calories = calories_per_gram - calories_without_water
print(f"{total_calories:.4f}")
