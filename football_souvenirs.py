team_name = input()
kind_gift = input()
bought_gift = int(input())
price = 0
team_is_valid = True
gift_is_valid = True
if team_name == "Argentina":
    if kind_gift == "flags":
        price = 3.25
    elif kind_gift == "caps":
        price = 7.20
    elif kind_gift == "posters":
        price = 5.10
    elif kind_gift == "stickers":
        price = 1.25
    else:
        gift_is_valid = False
elif team_name == "Brazil":
    if kind_gift == "flags":
        price = 4.20
    elif kind_gift == "caps":
        price = 8.50
    elif kind_gift == "posters":
        price = 5.35
    elif kind_gift == "stickers":
        price = 1.20
    else:
        gift_is_valid = False
elif team_name == "Croatia":
    if kind_gift == "flags":
        price = 2.75
    elif kind_gift == "caps":
        price = 6.90
    elif kind_gift == "posters":
        price = 4.95
    elif kind_gift == "stickers":
        price = 1.10
    else:
        gift_is_valid = False
elif team_name == "Denmark":
    if kind_gift == "flags":
        price = 3.10
    elif kind_gift == "caps":
        price = 6.50
    elif kind_gift == "posters":
        price = 4.80
    elif kind_gift == "stickers":
        price = 0.90
    else:
        gift_is_valid = False
else:
    team_is_valid = False


if team_is_valid == False:
    print("Invalid country!")
elif gift_is_valid == False:
    print("Invalid stock!")
else:
    total_sum = bought_gift * price
    print(f"Pepi bought {bought_gift} {kind_gift} of {team_name} for {total_sum:.2f} lv.")





