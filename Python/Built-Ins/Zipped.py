n, x = map(int, input().split())
all_grades = [list(map(float, input().split())) for _ in range(x)]
for student_grades in zip(*all_grades):
    print(sum(student_grades) / len(student_grades))
