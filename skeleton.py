minutes_race = int(input())
seconds_race = int(input())
length_track_meters = float(input())
seconds_per_100_meters = int(input())

total_seconds_race = minutes_race * 60 + seconds_race
reduced_time = length_track_meters / 120 * 2.5
racer_time = length_track_meters / 100 * seconds_per_100_meters - reduced_time

diff = abs(racer_time - total_seconds_race)
if racer_time <= total_seconds_race:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {racer_time:.3f}.")
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")