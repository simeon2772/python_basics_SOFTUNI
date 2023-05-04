from math import ceil
series_name = input()
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
free_time = break_time / 4
time_left = break_time - lunch_time - free_time

if time_left >= episode_time:
    time_after_episode = ceil(time_left - episode_time)
    print(f"You have enough time to watch {series_name} and left with {time_after_episode:.0f} minutes free time.")
elif time_left <= episode_time:
    time_needed = ceil(episode_time - time_left)
    print(f"You don't have enough time to watch {series_name}, you need {time_needed} more minutes.")
