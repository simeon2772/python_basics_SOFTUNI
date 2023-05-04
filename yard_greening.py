square_meters = float(input())
price_per_square_meter = 7.61
discount = 0.18
price_without_discount = square_meters * price_per_square_meter
price_with_discount = discount * price_without_discount
final_price = price_without_discount - price_with_discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {price_with_discount} lv.")