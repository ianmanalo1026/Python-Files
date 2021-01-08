class employee():
    raise_amount = 1.4

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def increase(self):
        self.pay = int(self.pay*self.raise_amount)


emp_1 = employee('Ian', 'Manalo', 50000)

print(emp_1.fullname())
print(emp_1.pay)
emp_1.increase()
print(emp_1.pay)
