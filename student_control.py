import json
class Student:
    def __init__(self, id, name, grades):
        self.id = id
        self.name = name
        self.grades = grades if grades else []

    def add_grades(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)
    
    def to_dict(self):
        student = {
            "id" : self.id,
            "name" : self.name,
            "grades" : self.grades
        }
        return student
    
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = []

    def add_students(self, student):
        self.students.append(student)
        self.safe_to_file()

    def remove_student(self, id):
        for i in range(len(self.students)):
            if id == self.students[i].id:
                self.students.pop(i)
                print("студент был удален")
                self.safe_to_file()
                return
        print("студент не найден")

    def find_student(self, id):
        for i in self.students:
            if id == i.id:
                return i
        return None

    def list_student(self):
        return self.students
    
    def safe_to_file(self):
        data = []
        for student in self.students:
            data.append(student.to_dict())
        with open(self.filename, "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self):
        students = []
        with open(self.filename, "r", encoding="UTF-8") as file:
            data = json.load(file)
            for d in data:
                student = Student(d["id"], d["name"], d["grades"])
                self.students.append(student)
        return students

def menu():
    sm = StudentManager()
    sm.load_from_file()
    while True:
        print("1.добавить студента")
        print("2.Удалить студента ")
        print("3.Показать всех студентов ")
        print("4.Добавить оценку ")
        print("5.Показать оценки студента ")
        print("6.Показать средний балл ")
        print("7.Выход")
        a = input("Выберите действие:")
        if a == "1":
            id = int(input("Введите id: "))
            name = input("введите имя: ")
            student = Student(id, name)
            sm.add_students(student)
            print("студент добавлен")
        elif a == "2":
            id = int(input("Введите id для удаления: "))
            sm.remove_student(id)
        elif a == "3":
            for i in sm.list_student():
                print(f'id:{i.id}, имя:{i.name}, оценки:{i.grades}')
        elif a == "4":
            id = int(input("введите id"))
            student = sm.find_student(id)
            g = int(input("Введите оценку:"))
            student.add_grades(g)
            sm.safe_to_file()
        elif a =="5":
            id = int(input("введите id"))
            student = sm.find_student(id)
            print(f"Оценки студента {student.name}: {student.grades}")
        elif a =="6":
            id = int(input(""))
            student = sm.find_student(id)
            print(f"Средний балл: {student.get_average()}")
        elif a =="7":
            break
        else:
            print("не то")


            


            




        