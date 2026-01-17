# class <class_name> :
    # def constructor <__init__> 
         # instance attribute 

    # class attributes 

    # class methods

# <object_name> = <class_name>()




# defining student class
class Student :
    # constructor parameterised constructor
    def __init__ (self, Name, Marks) :
        self.name = Name
        self.marks = Marks

    # class attributes 
    Standard = '5th'
    collegeName = 'ABC College'


    # class Methods
    def get_marks(self) :
        return self.marks


# instance / Object 
s1 = Student('pratham', 77) 
s2 = Student('yaksh', 50) 

# used object dot operator 
print(f"s1 object output : {s1.name}, standard : {s1.Standard}, college : {s1.collegeName}, marks : {s1.get_marks()}")

# used class Attribute with classname dot operator
print(f"s2 object output : {s2.name}, standard : {s2.Standard}, college : {Student.collegeName}, marks : {s2.get_marks()}")


# OUTPUT : 

# \FullStackDataScience> python -u "\Data-Science\python\OOPs\Class_Creation.py"
# s1 object output : pratham, standard : 5th, college : ABC College, marks : 77
# s2 object output : yaksh, standard : 5th, college : ABC College, marks : 50