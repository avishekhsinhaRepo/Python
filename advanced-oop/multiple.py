class Grade:
    def calculate_grade(self, average) -> str:
        if average >= 90:
            return "A+"
        elif 80 <= average < 90:
            return "A"
        elif 70 <= average < 80:
            return "B"
        elif 60 <= average < 70:
            return "C"
        elif 50 <= average < 60:
            return "D"
        else:
            return "F"


class Marks:
    def calculate_average(self) -> float:
        return sum(self.marks) / len(self.marks)


class Student(Grade, Marks):
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_profile(self):
        avg  = self.calculate_average()
        return f"Name: {self.name}, Average Marks: {avg} , Grade :{self.calculate_grade(avg)}"


student = Student('Alex', marks=[90, 80, 70, 60, 50])
print(student.print_profile())