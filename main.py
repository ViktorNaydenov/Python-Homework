import json
FILE_NAME = "dnevnik.json"

class Dnevnik():

    def __init__(self):
        self.students = {}

    def add_student(self, name, grades):
        if not type(grades) == list:
            print("Grade must be a list")

        self.students[name] = grades
        self.write()

    def write(self):
        with open(FILE_NAME, "w") as f:
            json.dump(self.students, f)

    def read(self):
        with open(FILE_NAME, "r") as f:
            self.students = json.load(f)


dnevnik = Dnevnik()
dnevnik.add_student("Viktor Naydenov", [5, 6, 4])
dnevnik.read()
print(dnevnik.students)
