failed_tries = int(input())
failed_times = 0
solved_problem_count = 0
grades_sum = 0
last_problem = ""
has_failed = True
while failed_times < failed_tries:
    problem_name = input()
    if problem_name == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_problem_count += 1
    last_problem = problem_name
if has_failed:
    print(f"You need a break, {failed_tries} poor grades.")
else:
    print(f"Average score: {grades_sum / solved_problem_count:.2f}")
    print(f"Number of problems: {solved_problem_count}")
    print(f"Last problem: {last_problem}")
