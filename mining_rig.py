from math import ceil
video_card = int(input())
adapter = int(input())
electricity_per_card_day = float(input())
profit_per_card_day = float(input())
count_video_cards = 13
count_adapters = 13
second_hand_machine = 1000

price_video_card = video_card * count_video_cards
price_adapter = adapter * count_adapters

money_total = price_adapter + price_video_card + second_hand_machine

day_profit = profit_per_card_day - electricity_per_card_day

total_profit_cards_per_day = count_video_cards * day_profit

investment_comeback = money_total / total_profit_cards_per_day

print(money_total)
print(ceil(investment_comeback))
