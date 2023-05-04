age = int(input())
washing_machine_price = float(input())
price_per_toy = int(input())

money = 10
count_toys = 0
sum = 0
brother_steal = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        count_toys += 1
    else:
        brother_steal += 1
        sum += money
        money += 10

result = sum + (count_toys * price_per_toy) - brother_steal

diff = abs(result - washing_machine_price)

if result >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")