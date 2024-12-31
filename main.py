import django_setup
from lesson.models import Subject, Teacher, Class, Student, Schedule, Grade


def add_subject(name, description):
    subject = Subject(name=name, description=description)
    subject.save()
    print(f"Subject {name} added")
    return subject


def add_teacher(teacher_name, teacher_last_name, subject_id):
    try:
        new_subject_id = Subject.objects.get(id=subject_id)
        teacher = Teacher(name=teacher_name, last_name=teacher_last_name,  subject=new_subject_id)
        teacher.save()
        print(f'Teacher {teacher_name} added')
    except Subject.DoesNotExists:
        print(f'Teacher with ID {subject_id} not found')


def add_class(class_name, year_of_study):
    class_ = Class(class_name=class_name, year_of_study=year_of_study)
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


def add_occupation_to_schedule(day_of_week, time_of_start, subject, class_, teacher):
    try:
        subject_id = Subject.objects.get(id=subject)
        class_id = Class.objects.get(id=class_)
        teacher_id = Teacher.objects.get(id=teacher)
        schedule = Schedule(day_of_week=day_of_week,
                            time_of_start=time_of_start,
                            subject=subject_id,
                            class_name=class_id,
                            teacher_name=teacher_id)
        schedule.save()
        print('Schedule was added')
    except Subject.DoesNotExists and Class.DoesNotExists and Teacher.DoesNotExists:
        print(f"Subject, Class and Teacher with ID {subject}, {class_}, {teacher} was not found")


def add_grade(student_id, subject_id, grade, date):
    try:
        student = Student.objects.get(id=student_id)
        subject = Subject.objects.get(id=subject_id)
        grade = Grade(student=student, subject=subject, grade=grade, date=date)
        grade.save()
        print("Grade was added!")
    except Student.DoesNotExists and Subject.DoesNotExists:
        print(f'Student and Subjects with ID {student_id}, {subject_id} was not found')


while True:
    print("\n1. Створити предмет")
    print("2. Створити вчителя")
    print("3. Створити клас")
    print("4. Створити студента")
    print("5. Додавання заняття в розклад")
    print("6. Додавання оцінки")
    print("7. Вийти")

    choice = int(input("Виберіть дію (1-5): "))

    if choice == 1:
        name = input("Введіть назву предмету: ")
        description = input("Введіть опис предмету: ")
        add_subject(name, description)

    elif choice == 2:
        name = input("Введіть ім'я вчителя: ")
        last_name = input("Введіть прізвище вчителя: ")
        subject_id = int(input("Введіть ID предмету: "))
        add_teacher(name, last_name, subject_id)

    elif choice == 3:
        class_name = input("Введіть назву класу: ")
        year_of_study = int(input("Введіть рік навчання (Кількість років): "))
        add_class(class_name, year_of_study)

    elif choice == 4:
        student_name = input("Введіть і'м'я студента: ")
        last_name = input("Введіть прізвище студента: ")
        class_id = int(input("Введіть ID класу: "))
        add_student(student_name, last_name, class_id)

    elif choice == 5:
        day_of_week = input("Введіть день тижня (Наприклад 'Понеділок'): ")
        time_of_start = input("Введіть час початку заняття (Наприклад '10:00'): ")
        subject = int(input("Введіть ID предмету: "))
        class_ = int(input("Введіть ID класу: "))
        teacher = int(input("Введіть ID вчителя: "))
        add_occupation_to_schedule(day_of_week, time_of_start, subject, class_, teacher)

    elif choice == 6:
        student = int(input("Введіть ID студента: "))
        subject = int(input("Введіть ID предмету: "))
        grade = int(input("Введіть оцінку: "))
        date = input("Введіть дату оцінки (Наприклад '2022-05-15'): ")
        add_grade(student, subject, grade, date)

    elif choice == 7:
        print("Завершення роботи")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")
