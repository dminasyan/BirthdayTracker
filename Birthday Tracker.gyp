import datetime as dt
import os
import sqlite3

# class BirthdayPerson:

#     def __init__(self, name, birthday):
#         self.name = name
#         self.bday = str(dt.datetime.strptime(birthday, '%m-%d-%Y'))[:10]


#     def __str__(self):
#         return self.name + "'s birthday is " + self.bday


# class BirthdayTracker:
    
#     def __init__(self):
#         self.birthdays = {}

#     def addPerson(self, BirthdayPerson):
#         self.birthdays[BirthdayPerson.name] = BirthdayPerson.bday
    
#     def retrieveBirthday(self, name):
#         return self.birthdays[name]

#     def __str__(self):
#         for name, bday in self.birthdays.items():
#             print("Name: " + name + "\nBirthday: " + bday)
#         return ''


if __name__ == "__main__":

    if not os.path.isfile("jsonTracker.db"):
        trackdb = sqlite3.connect("jsonTracker.db")
        t = trackdb.cursor()
        t.execute("CREATE TABLE bdays (Name, BirthDate)")

    print("You can quit anytime by hitting CRTL-C")
    try:
        while True:
            trackdb = sqlite3.connect("jsonTracker.db")
            t = trackdb.cursor()

            option = input("Adding or Retrieving ('A' or 'R')? \n")

            if option.upper() == 'A':
                #entering and creating a person
                name = input("Enter First and Last Name: \n")
                bday = input("Enter " + name + "'s Birthday (MM-DD-YYYY): \n")
                # person = BirthdayPerson(name, bday)

                #adding person to Database
                t.execute("INSERT INTO bdays VALUES (?,?)", (name, bday))


            elif option.upper() == 'R':
                name = input("Whose birthday would you like to know? \n")
                t.execute("SELECT BirthDate FROM bdays WHERE Name=?", (name,))
                retrievedBday = t.fetchall()
                print(retrievedBday)

            else:
                print("invalid")

    except KeyboardInterrupt:
        pass

    trackdb.commit()
    trackdb.close()
    
