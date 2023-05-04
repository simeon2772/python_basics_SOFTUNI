maiden_party = float(input())
love_letter = int(input())
roses = int(input())
key_chains = int(input())
paintings = int(input())
surprise_luck = int(input())
discount = 0
count_of_arti = love_letter + roses + key_chains + paintings + surprise_luck
total_sum = (love_letter * 0.60) + (roses * 7.20) + (key_chains * 3.60) + (paintings * 18.20) + (surprise_luck * 22)

if count_of_arti >= 25:
    discount = total_sum * 0.35

end_sum = total_sum - discount
fee_hosting = end_sum * 0.10
profit = end_sum - fee_hosting
diff = abs(profit - maiden_party)
if profit >= maiden_party:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
