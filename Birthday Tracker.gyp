import datetime as dt

class BirthdayPerson:

    def __init__(self, name, birthday):
        self.name = name
        self.bday = str(dt.datetime.strptime(birthday, '%m-%d-%Y'))[:10]


    def __str__(self):
        return self.name + "'s birthday is " + self.bday


class BirthdayTracker:
    
    def __init__(self, BirthdayPerson):
        self.birthdays = {}
        self.addPerson(BirthdayPerson)

    def addPerson(self, BirthdayPerson):
        self.birthdays[BirthdayPerson.name] = BirthdayPerson.bday

    def __str__(self):
        for name, bday in self.birthdays.items():
            print("Name: " + name + "\nBirthday: " + bday)
        return ''


if __name__ == "__main__":
    name = input("Enter First and Last Name: ")
    bday = input("Enter " + name + "'s Birthday (MM-DD-YYYY): ")
    person = BirthdayPerson(name, bday)
    tracker = BirthdayTracker(person)
    print(tracker)