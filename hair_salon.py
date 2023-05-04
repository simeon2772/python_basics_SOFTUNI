money_goal = int(input())
inline_input = input()
money_throughout_day = 0
while inline_input != "closed":
    if inline_input == "haircut":
        kind_of_haircut = input()
        if kind_of_haircut == "mens":
            money_throughout_day += 15
        elif kind_of_haircut == "ladies":
            money_throughout_day += 20
        elif kind_of_haircut == "kids":
            money_throughout_day += 10
    elif inline_input == "color":
        kind_of_color = input()
        if kind_of_color == "touch up":
            money_throughout_day += 20
        elif kind_of_color == "full color":
            money_throughout_day += 30
    if money_throughout_day >= money_goal:
        break
    inline_input = input()

diff = abs(money_goal - money_throughout_day)
if money_throughout_day >= money_goal:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {diff}lv. more.")

print(f"Earned money: {money_throughout_day}lv.")