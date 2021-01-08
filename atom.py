# Corey Schafer
# Python OOP Tutorial 1: Classes and Instances
# Python OOP Tutorial 2: Class Variables
# Python OOP Tutorial 3: classmethods and staticmethods - next


class Employee:
    # class is a blueprint of the system

    num_of_emps = 0  # class variables
    raise_amount = 1.04  # class variables

    # __init__ method is to initialize argument and instances. Instance is the first argument and the rest is argument.
    def __init__(self, first, last, pay):
        self.first = first  # method variables
        self.last = last  # method variables
        self.pay = pay  # method variables
        self.email = first + "." + last + "@company.com"  # method variables

        # will add 1 everytime we create employee. use Employee instead if no need to overwritten the data
        Employee.num_of_emps += 1

    def fullname(self):  # method
        # {} {} is use as an indicator or format of the instances
        return '{} {} {}'.format(self.first, self.last, self.pay)

    def apply_raise(self):
        # used int as the result is intergers. use self.raise_amount to overwritten the data
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee("Ian", "Manalo", 6000)
emp_2 = Employee("cardo", "dalisay", 7000)


print(emp_1.email)  # no need to put () because the method does not use return function
print(emp_1.fullname())  # () should be place after fullname to return the value.
# print(Employee.fullname(emp_1)) # print using class
# print(Employee.__dict__)
# print methods and variables within the class
print(emp_1.pay)
emp_1.apply_raise()  # applying raise to the employee
print(emp_1.pay)  # showing new pay of employee
print(Employee.num_of_emps)  # print out number of employee. should be put after employee created
