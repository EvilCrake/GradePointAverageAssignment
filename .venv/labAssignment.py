grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Создаем словарь, где ключом будет имя ученика, а значением - его средний балл
student_grades = {}

for i, student in enumerate(students):
    grades_sum = sum(grades[i])
    grades_len = len(grades[i])
    average_grade = grades_sum / grades_len
    student_grades[student] = average_grade

print(student_grades)
