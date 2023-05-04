pages = int(input())
pages_per_hour = int(input())
deadline_days = int(input())
hours_to_finish_book = pages // pages_per_hour
hours_per_day = hours_to_finish_book // deadline_days
print(hours_per_day)