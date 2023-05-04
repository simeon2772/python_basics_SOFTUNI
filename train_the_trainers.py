people_assessment = int(input())

line_input = input()
sum_all_grades = 0
count_grades = 0
while line_input != "Finish":
    presentation = line_input
    sum_current_grade_avr = 0

    for i in range(1, people_assessment + 1):
        current_grade = float(input())
        count_grades += 1
        sum_all_grades += current_grade
        sum_current_grade_avr += current_grade

    avr_grade_current = sum_current_grade_avr / people_assessment
    print(f"{presentation} - {avr_grade_current:.2f}.")

    line_input = input()
final_avr_grade = sum_all_grades / count_grades
print(f"Student's final assessment is {final_avr_grade:.2f}.")
