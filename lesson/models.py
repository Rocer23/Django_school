from django.db import models


# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Class(models.Model):
    class_name = models.CharField(max_length=200)

    def __str__(self):
        return self.class_name


class Student(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject.name}, {self.class_name}, {self.teacher.name}"


class Grade(models.Model):
    grade = models.CharField(max_length=1)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade}, {self.student.name}, {self.subject.name}"

