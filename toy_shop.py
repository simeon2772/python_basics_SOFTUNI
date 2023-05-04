holiday_price = float(input())
puzzle_price = int(input())
doll_price = int(input())
bear_price = int(input())
stuffed_toy_price = int(input())
truck_price = int(input())
discount = 0
toys_sum = (puzzle_price * 2.60) + (doll_price * 3) + (bear_price * 4.10) + (stuffed_toy_price * 8.20) + (truck_price * 2)
toys_count = puzzle_price + doll_price + bear_price + stuffed_toy_price + truck_price
if toys_count >= 50:
    discount = toys_sum * 0.25
total_sum = toys_sum - discount
rent = total_sum * 0.10
profit = total_sum - rent
money_left = profit - holiday_price
money_needed = abs(profit - holiday_price)
if profit >= holiday_price:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    print(f"Not enough money! {money_needed:.2f} lv needed.")




