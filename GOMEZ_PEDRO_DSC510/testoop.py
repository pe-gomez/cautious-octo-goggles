class employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay, temperatureK):
        self.first = first
        self.last = last
        self.pay = pay
        self.temperatureK = temperatureK
        self.email = first + '.' + last + '@company.com'
        self.temperatureF = round((temperatureK * 9 / 5) - 459.67)  # Kelvin to Fahrenheit converson

        employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * employee.raise_amount)  # can also use self.raise_amount if ind can change

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay,0)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first,self.last,self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay+other.pay

class developer(employee):

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang=prog_lang

class manager(employee):

    def __init__(self, first, last, pay,temperatureK, employees=None):
        super().__init__(first, last, pay,temperatureK)
        if employees is None:
            self.employees = []
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())

#print(help(developer))
#print(help(employee))

employee.set_raise_amt(1.05)

emp_1 = employee('corey', 'schafer', 50000, 271)
emp_2 = employee('test', 'user', 60000, 282)

mgr_1=manager('peg','smith',100000,0,[emp_1])

print(emp_1+emp_2)

print(isinstance(mgr_1,manager)) #tells if a class is a subclass of other

mgr_1.print_emps()
#
# first, last, pay = 'jon-doe-7000'.split('-')
# emp_3 = employee(first, last, pay, 200)
emp_3 = employee.from_string('jon-doe-7000')

print(emp_1.first, emp_1.email, emp_1.temperatureF)
print(emp_2.first, emp_2.email, emp_2.temperatureF)

print(emp_3)
print(emp_3.__dict__)
print (repr(emp_3))
print (str(emp_3))

print(1+2)
print(int.__add__(1,2))


'''
#from datetime \
import datetime
print (employee.is_workday(datetime.datetime.now()))
print (datetime.date(2019,11,3))

class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)
'''