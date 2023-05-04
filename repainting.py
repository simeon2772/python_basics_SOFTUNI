nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours_workers = int(input())
price_nylon = (nylon + 2) * 1.50
price_paint = (paint * 1.10) * 14.50
price_paint_thinner = paint_thinner * 5
price_bag = 0.40
total_sum_materials = price_nylon + price_paint + price_paint_thinner + price_bag
sum_workers = (total_sum_materials * 0.30) * hours_workers
total_sum = total_sum_materials + sum_workers
print(total_sum)









