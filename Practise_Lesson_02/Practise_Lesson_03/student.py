class Student:
    def __init__(self, first_name, surname, age,
course):
        self.first_name = first_name
        self.surname = surname
        self.age = age
        self.course = course

    def __str__(self):
        return f"{self.first_name} {self.surname}, {self.age} лет, курс: {self.course}"