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
        return cls(first, last, pay, 200)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


employee.set_raise_amt(1.05)

emp_1 = employee('corey', 'schafer', 50000, 271)
emp_2 = employee('test', 'user', 60000, 282)

# first, last, pay = 'jon-doe-7000'.split('-')
# emp_3 = employee(first, last, pay, 200)
emp_3 = employee.from_string('jon-doe-7000')

print(emp_1.first, emp_1.email, emp_1.temperatureF)
print(emp_2.first, emp_2.email, emp_2.temperatureF)

print(emp_3.__dict__)

#from datetime \
import datetime
print (employee.is_workday(datetime.datetime.now()))
print (datetime.date(2019,11,3))
