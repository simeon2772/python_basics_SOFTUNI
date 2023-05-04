line_input = input()
total_count_tickets = 0
student_count = 0
standard_count = 0
kid_count = 0
while line_input != "Finish":
    movie = line_input
    capacity = int(input())

    command_line = input()
    current_movie_counter = 0
    while command_line != "End":
        type_ticket = command_line
        total_count_tickets += 1
        current_movie_counter += 1
        if type_ticket == "student":
            student_count += 1
        elif type_ticket == "standard":
            standard_count += 1
        else:
            kid_count += 1

        if current_movie_counter == capacity:
            break
        command_line = input()
    percentage_current = current_movie_counter / capacity * 100
    print(f"{movie} - {percentage_current:.2f}% full.")
    line_input = input()

print(f"Total tickets: {total_count_tickets}")
percentage_student = student_count / total_count_tickets * 100
print(f"{percentage_student:.2f}% student tickets.")
percentage_standard = standard_count / total_count_tickets * 100
print(f"{percentage_standard:.2f}% standard tickets.")
percentage_kid = kid_count / total_count_tickets * 100
print(f"{percentage_kid:.2f}% kids tickets.")