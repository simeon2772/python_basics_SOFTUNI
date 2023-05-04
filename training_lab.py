width_meters = float(input())
length_meters = float(input())

cm_width = width_meters * 100
cm_length = length_meters * 100
corridor = 100
cm_length_without_corridor = cm_length - corridor
work_places_per_row_for_length = 11 * 70
total_cm_length_left = cm_length_without_corridor - work_places_per_row_for_length

work_places_per_row_for_width = 12 * 120
total_cm_width_left = cm_width - work_places_per_row_for_width

total_work_places = (11 * 12) - 3
print(total_work_places)
