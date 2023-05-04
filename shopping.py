budget = float(input())
video_cards = int(input())
processors = int(input())
ram_memory = int(input())

video_cards_price = video_cards * 250
price_per_processor = video_cards_price * 0.35
processors_price = processors * price_per_processor
price_per_ram_memory = video_cards_price * 0.10
price_ram_memory = ram_memory * price_per_ram_memory

total_sum = video_cards_price + processors_price + price_ram_memory
if video_cards > processors:
    total_sum = total_sum * 0.85

money_left = budget - total_sum
if total_sum <= budget:
    print(f"You have {money_left:.2f} leva left!")
elif total_sum > budget:
    money_needed = total_sum - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")

