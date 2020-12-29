import datetime as dt
import json
import os
import sqlite3

class BirthdayPerson:

    def __init__(self, name, birthday):
        self.name = name
        self.bday = str(dt.datetime.strptime(birthday, '%m-%d-%Y'))[:10]


    def __str__(self):
        return self.name + "'s birthday is " + self.bday


class BirthdayTracker:
    
    def __init__(self):
        self.birthdays = {}

    def addPerson(self, BirthdayPerson):
        self.birthdays[BirthdayPerson.name] = BirthdayPerson.bday

    def __str__(self):
        for name, bday in self.birthdays.items():
            print("Name: " + name + "\nBirthday: " + bday)
        return ''


if __name__ == "__main__":
    name = ""
    tracker = BirthdayTracker()
    print("You can quit anytime by hitting CRTL-C")
    try:
        while True:
            name = input("Enter First and Last Name: \n")
            bday = input("Enter " + name + "'s Birthday (MM-DD-YYYY): \n")
            person = BirthdayPerson(name, bday)
            tracker.addPerson(person)
    except KeyboardInterrupt:
        pass

    if not os.path.isfile("jsonTracker.db"):
        trackdb = sqlite3.connect("jsonTracker.db")
        t = trackdb.cursor()
        t.execute("CREATE TABLE bdays (Name, BirthDate)")
        
    trackdb = sqlite3.connect("jsonTracker.db")
    t = trackdb.cursor()
    t.execute("INSERT INTO bdays VALUES (?,?)", (name, bday))
    trackdb.commit()
    trackdb.close()
    
    # if not os.path.isfile("jsonTracker.json"):
    #     with open('jsonTracker.json') as jFile:
    #         json.dump(tracker.birthdays, jFile)
    # else:
    #     with open("jsonTracker.json") as jFile:
    #         bdayData = json.load(jFile)
    #     bdayData.update(tracker.birthdays)
    #     with open("jsonTracker.json", "w") as jFile:
    #         json.dump(bdayData, jFile)
    