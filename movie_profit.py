movie_name = input()
days = int(input())
tickets = int(input())
price_tickets = float(input())
percentage_for_cinema = int(input())

ticket_price_per_day = tickets * price_tickets
income_days = days * ticket_price_per_day
percentage = income_days * percentage_for_cinema/100
total_income = income_days - percentage
print(f"The profit from the movie {movie_name} is {total_income:.2f} lv.")