chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())
delivery = 2.50
price_chicken_menu = chicken_menu * 10.35
price_fish_menu = fish_menu * 12.40
price_vegan_menu = vegan_menu * 8.15
whole_menu_price = price_vegan_menu + price_chicken_menu + price_fish_menu
desert = whole_menu_price * 0.20
total_menu_price = whole_menu_price + desert + delivery
print(total_menu_price)









