deposit_amount = float(input())
month = int(input())
annual_rate = float(input())
per_year = deposit_amount * (annual_rate/100)
per_month = per_year / 12
total_sum = deposit_amount + (per_month * month)
print(total_sum)



