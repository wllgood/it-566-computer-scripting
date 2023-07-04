from person import Person

class Student(Person): #Student extends Person class and provides its own constructors

    def __init__(self, firstName, middleName, lastName, studentID, major):
        # Constructor chaining
        super().__init__(firstName, middleName, lastName)
        # Then set derived class properties
        self.student_id = studentID
        self.major = major

    def __str__(self):
        return super().__str__() + " " + self.student_id + " " + self.major