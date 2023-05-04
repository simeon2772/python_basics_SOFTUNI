price_per_kilo_vegi = float(input())
price_per_kilo_fruit = float(input())
total_kilo_vegi = float(input())
total_kilo_fruit = float(input())

total_price_vegi = price_per_kilo_vegi * total_kilo_vegi
total_price_fruit = price_per_kilo_fruit * total_kilo_fruit

total_sum = total_price_fruit + total_price_vegi

total_sum_in_euro = total_sum / 1.94

print(f"{total_sum_in_euro:.2f}")