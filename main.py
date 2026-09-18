import json
from abc import ABC, abstractmethod
from pathlib import Path


database ="School_management_system.json"
data ={"Students":[],"Teachers":[]}

def save():
    with open(database,"w") as f:
        json.dump(data,f)

if Path(database).exists():
    with open(database, 'r') as f:
        content = f.read()
        if content:
            data=json.loads(content)



class Person(ABC):

    @abstractmethod
    def roles(self):
        pass
    @abstractmethod
    def Register(self):
        pass
    @abstractmethod
    def Details(self):
        pass

    @staticmethod
    def Validate_email(email):
        if "@" in email and "." in email:
            return True

        else:
            return False



class Student(Person):
    def roles(self):
        return "Student"
    def Register(self):
        name = str(input("Please enter your name:-  "))
        age = int(input("Please enter your age:-  "))
        gender = str(input("Please enter your gender:-  "))
        email = str(input("Please enter your email:-  "))
        roll_no = int(input("Please enter your roll:-  "))
        if gender == "Male" or gender == "M" or gender == "m" or gender == "male":
            return "Male"
        elif gender == "Female" or gender == "F" or gender == "f" or gender == "female":
            return "Female"
        else:
            print("Unknown")

        if not Person.Validate_email(email):
            print("Please enter a valid email address")

        else:
            return email

        for i in data['Student']:
            if i['roll_no'] == roll_no:
                print("Student allready exist!!")
                return
        data['Students'].append({'name': name, 'age': age, 'gender': gender, 'roll_no': roll_no, 'email': email,'grade' : {}})
class Teachers(Person):
    def roles(self):
        return "Teacher"
    def Register(self):
        name = str(input("Please enter your name:-  "))
        age = int(input("Please enter your age:-  "))
        gender = str(input("Please enter your gender:-  "))
        email = str(input("Please enter your email:-  "))
        Emp_no = int(input("Please enter your Employee no:-  "))
        if gender == "Male" or gender == "M" or gender == "m" or gender == "male":
            return "Male"
        elif gender == "Female" or gender == "F" or gender == "f" or gender == "female":
            return "Female"
        else:
            print("Unknown")

        if not Person.Validate_email(email):
            print("Please enter a valid email address")

        else:
            return email

        for i in data['Teacher']:
            if i['Emp_no'] == Emp_no:
                print("Student already exist!!")
                return

        data['Teachers'].append({ 'name' : name,'age' : age,'gender' : gender,'Emp_no' : Emp_no,'email' : email,'subject':{}})


print("Press 1 to Register student.")
print("Press 2 to Register teacher.")
print("Press 3 to add marks of student.")
print("Press 4 for student details.")
print("Press 5 for teacher details.")


user = int(input("Please Enter your choice(1 to 5):-  "))




if user == 1:
    pass
elif user == 2:
    pass
elif user == 3:
    pass
elif user == 4:
    pass
elif user == 5:
    pass
else:
    print("Please enter your choice between 1 to 5 :-")