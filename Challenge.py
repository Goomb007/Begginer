from typing import Union, Any, Tuple

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
grades_Aaron = sum(grades[0]) / len(grades[0])
grades_Bilbo = sum(grades[1]) / len(grades[1])
grades_Johnny = sum(grades[2]) / len(grades[2])
grades_Khendrik = sum(grades[3]) / len(grades[3])
grades_Steve = sum(grades[4]) / len(grades[4])
grades_average = []
grades_average.append(grades_Aaron)
grades_average.append(grades_Bilbo)
grades_average.append(grades_Johnny)
grades_average.append(grades_Khendrik)
grades_average.append(grades_Steve)
students.sort()
students_grades = zip(students, grades_average)
print(dict(students_grades))
