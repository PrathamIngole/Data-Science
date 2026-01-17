# to delete an attribute or a whole object we have delete keyword

class Car:
    def __init__(self) :
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self) :
        self.clutch = True
        self.acc = True
        print("car started ... ")

    def stop(self) :
        self.brk = True
        self.acc = False
        print("car stopped ...")


car1 = Car() 
print(car1.brk)
# first it will print brk value which is - False 

del car1.brk # or we can delete a whole object 
# del car1
# after delete it will show error 
print(car1.brk)


# OUTPUT :

# \Data-Science\python\OOPs\delete.py"
# Traceback (most recent call last):
#   File "Data-Science\python\OOPs\delete.py", line 22, in <module>
#     print(car1.brk)
#           ^^^^^^^^
# AttributeError: 'Car' object has no attribute 'brk'
# PS FullStackDataScience> python -u "\Data-Science\python\OOPs\delete.py"
# False
# Traceback (most recent call last):
#   File "Data-Science\python\OOPs\delete.py", line 23, in <module>
#     print(car1.brk)
#           ^^^^^^^^
# AttributeError: 'Car' object has no attribute 'brk'


