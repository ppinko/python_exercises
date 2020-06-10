"""
https://edabit.com/challenge/S7rdJsn6vkfC9BzcR
"""

" little cheasy solution"

class Employee:
    def __init__(self, full_name, **kwargs):
        self.firstname = full_name.split()[0]
        self.lastname = full_name.split()[1]
        for k, v in kwargs.items():
            if k == 'salary':
                self.salary = v
            elif k == 'height':
                self.height = v
            elif k == 'nationality':
                self.nationality = v
            elif k == 'subordinates':
                self.subordinates = v


" Alternative solution 1 "


class Employee:

    def __init__(self, full_name, **kwargs):
        self.full_name = full_name
        self.name, self.lastname = full_name.split()
        self.__dict__.update(kwargs)

" Alternative solution 2 "

class Employee:

    def __init__(self, str_names, **kwargs):
        _name, _lastname = str_names.split()
        self.name = _name
        self.lastname = _lastname
        for key, val in kwargs.items():
            setattr(self, key, val)


john = Employee('John Doe')
mary = Employee('Mary Major', salary=120000)
richard = Employee('Richard Roe', salary=110000, height=178)
giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese', subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])


assert john.lastname == 'Doe'
assert mary.salary == 120000
assert richard.height == 178
assert giancarlo.nationality == 'Italian'
assert peng.subordinates == ['Doe', 'Major', 'Roe', 'Rossi']

print("Success")