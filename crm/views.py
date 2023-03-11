from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from crm.models import Student, Teacher, Subject, Group, Visit, Lesson
from datetime import datetime
import json



# STUDENTS
def students(request):
    if request.method == 'GET':
        data = list(Student.objects.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        r = json.loads(request.body)
        student = Student()

        try:
            student.name = r['name']
            student.surname = r['surname']
            student.gender = r['gender']
            student.age = r['age']
        except KeyError:
            return JsonResponse({"success":False, "error":"request isn't full"})

        student.save()
        return JsonResponse({"success":True})


# TEACHERS
def teachers(request):
    if request.method == 'GET':
        data = list(Teacher.objects.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        r = json.loads(request.body)
        teacher = Teacher()

        try:
            teacher.name = r['name']
            teacher.surname = r['surname']
            teacher.gender = r['gender']
            teacher.age = r['age']
            teacher.desc = r['desc']
        except KeyError:
            return JsonResponse({"success":False, "error":"request isn't full"})

        teacher.save()
        return JsonResponse({"success":True})


# SUBJECTS
def subjects(request):
    if request.method == 'GET':
        data = list(Subject.objects.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        r = json.loads(request.body)
        subject = Subject()

        try:
            subject.name = r['name']
        except KeyError:
            return JsonResponse({"success":False, "error":"request isn't full"})

        try:
            if Subject.objects.get(name=subject.name):
                return JsonResponse({"success":False, "error":"subject exists"})
        except:
            subject.save()

        return JsonResponse({"success":True})


# GROUPS
def groups(request):
    if request.method == 'GET':
        data = list(Group.objects.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        r = json.loads(request.body)
        group = Group()

        try:
            group.name = r['name']
            teacher_id = r['teacher_id']
            subject_id = r['subject_id']
        except KeyError:
            return JsonResponse({"success":False, "error":"request isn't full"})

        try:
            if Group.objects.get(name=group.name):
                return JsonResponse({"success":False, "error":"group exists"})
        except:
            try:
                group.teacher = Teacher.objects.get(id=teacher_id)
                group.subject = Subject.objects.get(id=subject_id)
                group.save()
            except:
                return JsonResponse({"success":False, "error":"no such teacher or subject"})

        return JsonResponse({"success":True})


# LESSONS
def lessons(request):
    if request.method == 'GET':
        data = list(Lesson.objects.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        r = json.loads(request.body)
        lesson = Lesson()

        try:
            group = r["group"]
            date = r["date"]
        except KeyError:
            return JsonResponse({"success":False, "error":"request isn't full"})

        try:
            lesson.group = Group.objects.get(id=group)
        except:
            return JsonResponse({"success":False, "error":"no such group"})

        try:
            date = datetime(date["year"], date["month"], date["day"], date["hour"], date["minute"])
            lesson.datetime = date
        except:
            return JsonResponse({"success":False, "error":"wrong datetime representation"})

        lesson.save()
        return JsonResponse({"success":True})


# VISITS
def visits(request):
    if request.method == 'GET':
        data = list(Visit.objects.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        r = json.loads(request.body)
        visit = Visit()

        try:
            student = r['student']
            lesson = r['lesson']
        except KeyError:
            return JsonResponse({"success":False, "error":"request isn't full"})

        try:
            visit.student = Student.objects.get(id=student)
            visit.lesson = Lesson.objects.get(id=lesson)
        except:
            return JsonResponse({"success":False, "error":"no such student or lesson"})

        try:
            if Visit.objects.get(student=visit.student, lesson=visit.lesson):
                return JsonResponse({"success":False, "error":"visit already exists"})
        except:
            visit.save()

        return JsonResponse({"success":True})

