packs_pencils = int(input())
packs_markers = int(input())
liters_for_board = int(input())
discount = int(input())
price_of_pencils = 5.80
price_of_markers = 7.20
price_per_liter = 1.20
packs_pencils = packs_pencils * price_of_pencils
packs_markers = packs_markers * price_of_markers
liters_for_board = liters_for_board * price_per_liter
total_amount = packs_markers + packs_pencils + liters_for_board
total_amount_discount = total_amount -(total_amount * (discount/100))
print(total_amount_discount)