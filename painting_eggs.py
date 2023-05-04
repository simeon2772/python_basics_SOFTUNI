eggs_size = input()
egg_color = input()
basket_eggs = int(input())
price = 0
if eggs_size == "Large":
    if egg_color == "Red":
        price = 16
    elif egg_color == "Green":
        price = 12
    elif egg_color == "Yellow":
        price = 9
elif eggs_size == "Medium":
    if egg_color == "Red":
        price = 13
    elif egg_color == "Green":
        price = 9
    elif egg_color == "Yellow":
        price = 7
elif eggs_size == "Small":
    if egg_color == "Red":
        price = 9
    elif egg_color == "Green":
        price = 8
    elif egg_color == "Yellow":
        price = 5

total_sum = basket_eggs * price
end_sum = total_sum * 0.65
print(f"{end_sum:.2f} leva.")