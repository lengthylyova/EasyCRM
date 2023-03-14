from django.db import models



# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    age = models.IntegerField()


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    age = models.IntegerField()
    desc = models.CharField(max_length=400)


class Subject(models.Model):
    name = models.CharField(max_length=40)


class Group(models.Model):
    name = models.CharField(max_length=20)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='groups', default=None)
    students = models.ManyToManyField(Student, related_name='groups')


class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, default=None, null=True)
    datetime = models.DateTimeField(auto_now_add=False, null=True, default=None)


class Visit(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='visits')
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, related_name='visits', null=True)


class Subscription(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subscription')
    first_day = models.DateTimeField(auto_now_add=True)
    last_day = models.DateTimeField(auto_now_add=False, null=True, default=None)
    lessons_left = models.IntegerField()
