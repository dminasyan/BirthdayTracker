import datetime as dt

class BirthdayStorage:

    def __init__(self, name, birthday):
        self.name = name
        self.bday = dt.datetime.strptime(birthday, '%Y-%m-%d')


    def __str__(self):
        return self.name + "'s birthday is " + str(self.bday)



ex = BirthdayStorage('David', '1999-01-07')
print(ex)
