class Employee:

   raise_amout = 1.04

   def __init__(self,first ,last ,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+ last + '@company.com'

   def fullname(self):
       return '{} {}'.format(self.first,self.last)

   def apply_raise(self):
       self.pay = int(self.pay * self.raise_amout)


   @classmethod                             #<- classmethod OTAN ANEFEROMASTE STO CLASS(cls) px Employee
   def set_raise_amt(cls,amount):
       cls.raise_amout = amount

   @classmethod
   def from_string(cls, emp_str):
       first, last, pay = emp_str.split('-')
       return cls(first,last,pay)

   @staticmethod                            #<- staticmethod otan aneferomaste se parametro pou den epireazei to class 
   def is_workday(day):
       if day.weekday() == 5 or day.weekday() == 6:
           return False
       return True

import datetime
my_date = datetime.date(2016, 7, 11)


class Developer(Employee):
    raise_amout = 1.10

    def __init__(self,first ,last ,pay, prog_lang):
        super().__init__(first ,last ,pay)
        self.prog_lang = prog_lang

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')


class Manager(Employee):
    def __init__(self,first ,last ,pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employess = []
        else:
            self.employess = employees

    def add_emp(self, emp):
        if emp not in self.employess:
            self.employess.append(emp)

    def remove_emp(self, emp):

        if emp in self.employess:
            self.employess.remove(emp)

    def print_emps(self):
        for emp in self.employess:
            print('-->', emp.fullname())


mgr_1 = Manager('Sue','Smith',10000,[dev_1])

print(mgr_1.email)

