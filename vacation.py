needed_money = float(input())
initial_money = float(input())
days_counter = 0
spending_counter = 0

while initial_money < needed_money and spending_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1
    if command == "save":
        initial_money += money
        spending_counter = 0
    elif command == "spend":
        initial_money -= money
        spending_counter += 1
        if initial_money < 0:
            initial_money = 0

if spending_counter == 5:
    print("You can't save the money.")
    print(days_counter)
if initial_money >= needed_money:
    print(f"You saved the money for {days_counter} days.")