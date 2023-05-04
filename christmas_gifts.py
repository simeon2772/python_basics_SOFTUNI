command = input()
counter_kids = 0
counter_adult = 0
toy_price = 5
sweater_price = 15
while command != "Christmas":
    age_member = int(command)
    if age_member <= 16:
        counter_kids += 1
    else:
        counter_adult += 1
    command = input()


money_for_toys = counter_kids * toy_price
money_for_sweater = counter_adult * sweater_price
print(f"Number of adults: {counter_adult}")
print(f"Number of kids: {counter_kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweater}")