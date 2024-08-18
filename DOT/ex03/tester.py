from new_student import Student

try:
    student = Student(name = "Edward", surname = "agle")
    print(student)
    print('----------------')
    student = Student(name = "Edward", surname = "agle", id = "toto")
    print(student)
except TypeError as terr:
    print(terr)