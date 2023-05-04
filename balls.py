number_of_balls = int(input())
total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
divides_balls = 0
others_balls = 0

for balls in range(number_of_balls):
    current_ball = input()
    if current_ball == "red":
        total_points += 5
        red_balls += 1
    elif current_ball == "orange":
        total_points += 10
        orange_balls += 1
    elif current_ball == "yellow":
        total_points += 15
        yellow_balls += 1
    elif current_ball == "white":
        total_points += 20
        white_balls += 1
    elif current_ball == "black":
        total_points //= 2
        divides_balls += 1
    else:
        others_balls += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {others_balls}")
print(f"Divides from black balls: {divides_balls}")


