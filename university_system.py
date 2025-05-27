class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Course: {self.course}")

class Lecturer(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Staff(Person):
    def __init__(self, name, age, staff_id, position):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Staff id: {self.staff_id}, Position: {self.position}")




student1= Student("Nassiwa hafswa", 22, 2300723750,"Software Engineering") 
lecturer1= Lecturer("Mukuba Sulait",45,"Networks")
staff1= Staff("Namubiru Aidah", 53, 552,"Dean of students")

print("Student information")
student1.display_info()

print("lecturer information")
lecturer1.display_info()

print("staff information")
staff1.display_info()