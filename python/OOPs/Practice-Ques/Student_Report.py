# Create Student class that takes name & marks of 3 subjects as a argument in constructor. then create a method to print the average.


# method 1
class Student_Report :
    def __init__(self, name, maths_marks, phy_marks, chem_marks):
        self.name = name
        self.maths_marks = maths_marks
        self.phy_marks = phy_marks
        self.chem_marks = chem_marks

    def calculate_Avg(self) :
        return (self.chem_marks + self.maths_marks + self.phy_marks) // 3
    
# method 2
class Student: 
    def __init__ (self, name, marks) :
        self.name = name
        self.marks = marks
    
    def get_avg(self) :
        sum = 0
        for mark in self.marks :
            sum += mark

        print(f"Hey!!! {self.name}, your avg marks is {sum/3}\n")
        


s1 = Student_Report("Pratham", 95, 82, 90)

print(f"student s1 name : {s1.name},\nmaths marks : {s1.maths_marks},\nphysics marks : {s1.phy_marks},\nchemistry marks : {s1.chem_marks}\n\nAverage of marks is : {s1.calculate_Avg()}\n\n")


# OUTPUT : 

# FullStackDataScience> python -u "\Data-Science\python\OOPs\student_report.py"

# student s1 name : Pratham,
# maths marks : 95,
# physics marks : 82,
# chemistry marks : 90

# Average of marks is : 89


marks_of_yaksh = [75, 84, 90]
s2 = Student("Yaksh", marks_of_yaksh)

print(f"By second method ")
s2.get_avg()

# OUTPUT : 

# By second method
# Hey!!! Yaksh, your avg marks is 83.0