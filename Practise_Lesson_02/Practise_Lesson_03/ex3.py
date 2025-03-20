
from student import Student
from coursegroup import CourseGroup

student = Student("Анна", "Иванова", 20, "Инженер")
classmate1 = Student("Олег", "Петров", 19, "Инженер")
classmate2 = Student("Виктория", "Лемон", 26, "Инженер")
classmate3 = Student("Леонид", "Мошкин", 29, "Инженер")

course_group = CourseGroup(student, [classmate1,classmate2,classmate3])

print(course_group)