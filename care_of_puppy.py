dog_food_kg = int(input())
command = input()
dog_food_in_grams = dog_food_kg * 1000
food_eaten_dog = 0
while command != "Adopted":
    current_food_day = int(command)
    dog_food_in_grams -= current_food_day
    command = input()

if dog_food_in_grams < 0:
    print(f"Food is not enough. You need {abs(dog_food_in_grams)} grams more.")
else:
    print(f"Food is enough! Leftovers: {dog_food_in_grams} grams.")

