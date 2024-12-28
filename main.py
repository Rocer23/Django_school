import django_setup
from lesson.models import Subject, Teacher, Class, Student


def add_subject(name):
    subject = Subject(name=name)
    subject.save()
    print(f"Subject {name} added")
    return subject


def add_teacher(teacher_name, subject_id):
    try:
        new_subject_id = Subject.objects.get(id=subject_id)
        teacher = Teacher(name=teacher_name, subject=new_subject_id)
        teacher.save()
        print(f'Teacher {teacher_name} added')
    except Subject.DoesNotExists:
        print(f'Teacher with ID {subject_id} not found')


def add_class(class_name):
    class_ = Class(class_name=class_name)
    class_.save()
    print(f"Class {class_name} added")


def add_student(student_name, last_name, class_id):
    try:
        new_class_id = Class.objects.get(id=class_id)
        student = Student(name=student_name, last_name=last_name, class_name=new_class_id)
        student.save()
        print(f'Student {student_name} added')
    except Class.DoesNotExists:
        print(f'Student with ID {class_id} not found')


while True:
    print("\n1. Створити предмет")
    print("2. Створити вчителя")
    print("3. Створити клас")
    print("4. Створити студента")
    print("5. Вийти")

    choice = int(input("Виберіть дію (1-5): "))

    if choice == 1:
        name = input("Введіть назву предмету: ")
        add_subject(name)

    elif choice == 2:
        name = input("Введіть ім'я вчителя: ")
        subject_id = int(input("Введіть ID предмету: "))
        add_teacher(name, subject_id)

    elif choice == 3:
        class_name = input("Введіть назву класу: ")
        add_class(class_name)

    elif choice == 4:
        student_name = input("Введіть і'м'я студента: ")
        last_name = input("Введіть прізвище студента: ")
        class_id = int(input("Введіть ID класу: "))
        add_student(student_name, last_name, class_id)

    elif choice == 5:
        print("Завершення роботи")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
