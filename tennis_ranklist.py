from math import floor
count_tournaments = int(input())
initial_points = int(input())
copy_initial_point = initial_points
tournament_won = 0
for i in range(1, count_tournaments + 1):
    current_tournament = input()
    if current_tournament == "W":
        copy_initial_point += 2000
        if current_tournament == "W":
            tournament_won += 1
    elif current_tournament == "F":
        copy_initial_point += 1200
    elif current_tournament == "SF":
        copy_initial_point += 720
aftermath_points = copy_initial_point
average_points = (aftermath_points - initial_points) / count_tournaments
percent_won_tournaments = (tournament_won / count_tournaments) * 100

print(f"Final points: {aftermath_points}")
print(f"Average points: {floor(average_points)}")
print(f"{percent_won_tournaments:.2f}%")
