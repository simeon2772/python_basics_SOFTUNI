from math import floor
record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

goal = distance_meters * seconds_per_meter
delay = floor(distance_meters / 15) * 12.5
total_time = goal + delay
competitor_time = total_time - record_seconds

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
elif total_time >= record_seconds:
    print(f"No, he failed! He was {competitor_time:.2f} seconds slower.")



