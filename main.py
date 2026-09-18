import json
from abc import ABC, abstractmethod
from pathlib import Path


database ="School_management_system.json"
data ={"Students":[],"Teachers":[]}



if Path(database).exists():
    with open(database, 'r') as f:
        content = f.read()
        if content:
            data=json.loads(content)

def save():
    with open(database,"w") as f:
        json.dump(data,f,indent=4)



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
        if gender == "Male" or gender == "M" or gender == "m" or gender == "male":
           gender ="Male"
        elif gender == "Female" or gender == "F" or gender == "f" or gender == "female":
            gender ="Female"
        else:
            print("Unknown")

        email = str(input("Please enter your email:-  "))
        if not Person.Validate_email(email):
            print("Please enter a valid email address")
            return



        roll_no = int(input("Please enter your roll:-  "))
        for i in data['Students']:
            if i['roll_no'] == roll_no:
                print("Student already exist!!")
                return
        data['Students'].append({'name': name, 'age': age,'email':email, 'gender': gender, 'roll_no': roll_no,'grade' : {}})
        save()
        print(f"{name} has been added to the database")
    def Details(self):
        pass
    def add_grade(self):
        roll_no = int(input("Please enter your roll:-  "))
        subject = str(input("Please enter your subject:-  "))
        marks = int(input("Please enter your grade:-  "))

        for i in data['Students']:
            if i['roll_no'] == roll_no:
                i['grade'][subject]=marks
                save()
                print("marks are add successfully !!! ")
                return

        print("student not found!!!")





class Teachers(Person):
    def roles(self):
        return "Teacher"
    def Register(self):
        name = str(input("Please enter your name:-  "))
        age = int(input("Please enter your age:-  "))
        gender = str(input("Please enter your gender:-  "))
        subject = str(input("Please enter your subject:-  "))

        if gender == "Male" or gender == "M" or gender == "m" or gender == "male":
            gender= "Male"
        elif gender == "Female" or gender == "F" or gender == "f" or gender == "female":
            gender ="Female"
        else:
            print("Unknown")


        email = str(input("Please enter your email:-  "))
        if not Person.Validate_email(email):
            print("Please enter a valid email address")
            return
        emp_no = int(input("Please enter your Employee no:-  "))
        for i in data['Teachers']:
            if i['Emp_no'] == emp_no:
                print("Teacher already exist!!")
                return

        data['Teachers'].append({ 'name' : name,'age' : age,'gender' : gender,'Emp_no' : emp_no,'email' : email,'subject':subject})
        save()
        print(f"{name} has been added to the database")
    def Details(self):
            pass


stud = Student()
teach = Teachers()
print("Press 1 to Register student.")
print("Press 2 to Register teacher.")
print("Press 3 to add marks of student.")
print("Press 4 for student details.")
print("Press 5 for teacher details.")


user = int(input("Please Enter your choice(1 to 5):-  "))




if user == 1:
    stud.Register()
elif user == 2:
    teach.Register()
elif user == 3:
    stud.add_grade()
elif user == 4:
    stud.Details()
elif user == 5:
    teach.Details()
else:
    print("Please enter your choice between 1 to 5 :-")