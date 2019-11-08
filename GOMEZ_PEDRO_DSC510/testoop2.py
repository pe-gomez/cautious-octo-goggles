# demonstrating property decorator in classes

class employee:

    def __init__(self, first, last, pay, temperatureK):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@company.com'

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.first=first
        self.last=last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first=None
        self.last=None


emp_1 = employee('corey', 'schafer', 50000, 271)
emp_1.fullname="bill board"

del emp_1.fullname

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
