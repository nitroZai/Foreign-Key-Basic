from django.db import models

class Subjects(models.Model):
    semester = models.CharField(max_length=2)
    subject1 = models.CharField(max_length=20)
    subject2 = models.CharField(max_length=20)
    subject3 = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.semester


class Student(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    semester = models.ForeignKey(Subjects, on_delete=models.PROTECT)
    branch = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Marks(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    subject1 = models.CharField(max_length=20)
    subject2 = models.CharField(max_length=20)
    subject3 = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.student)