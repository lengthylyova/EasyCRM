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


def sp_student(request, id):
    if request.method == 'GET':
        data = list(Student.objects.filter(id=id).values())
        if not data:
            return JsonResponse({"success":False, "error":"no such student"})
        return JsonResponse(data, safe=False)


def sp_student_groups(request, id):
    try:
        student = Student.objects.get(id=id)
    except:
        return JsonResponse({"success":False, "error":"no such student"})

    if request.method == 'GET':
        data = list(student.groups.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        r = json.loads(request.body)
        try:
            group_id = r['group_id']
        except:
            return JsonResponse({"success":False, "error":"request isn't full"})

        try:
            student.groups.get(id=group_id)
            return JsonResponse({"success":False, "error":"student already in group"})
        except:
            student.groups.add(group_id)
            student.save()
            
        return JsonResponse({"success":True})


def sp_student_visits(request, id):
    try:
        student = Student.objects.get(id=id)
    except:
        return JsonResponse({"success":False, "error":"no such student"})

    if request.method == 'GET':
        data = list(student.visits.values())
        return JsonResponse(data, safe=False)


def sp_student_group_delete(request, student_id, group_id):
    try:
        student = Student.objects.get(id=student_id)
    except:
        return JsonResponse({"success":False, "error":"no such student"})

    if request.method == 'GET':
        return JsonResponse({'saccess':False, "error":"wrong request method"})

    if request.method == 'POST':
        try:
            student.groups.remove(Group.objects.get(id=group_id))
        except:
            return JsonResponse({"saccess":False, "error":"student not in group"})

        return JsonResponse({"success":True})


def sp_student_delete(request, id):
    if request.method == 'GET':
        return JsonResponse({'saccess':False, "error":"wrong request method"})

    if request.method == 'POST':
        try:
            student = Student.objects.get(id=id)
        except:
            return JsonResponse({"success":False, "error":"no such student"})

        student.delete()
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


def sp_teacher(request, id):
    if request.method == 'GET':
        data = list(Teacher.objects.filter(id=id).values())
        if not data:
            return JsonResponse({"success":False, "error":"no such teacher"})
        return JsonResponse(data, safe=False)


def sp_teacher_groups(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
    except:
        return JsonResponse({"success":False, "error":"no such teacher"})

    if request.method == 'GET':
        data = list(teacher.groups.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        r = json.loads(request.body)
        try:
            group_id = r['group_id']
        except:
            return JsonResponse({"success":False, "error":"request isn't full"})

        try:
            teacher.groups.get(id=group_id)
            return JsonResponse({"success":False, "error":"teacher already owns this group"})
        except:
            teacher.groups.add(group_id)
            teacher.save()

        return JsonResponse({"success":True})


def sp_teacher_delete(request, id):
    if request.method == 'GET':
        return JsonResponse({'saccess':False, "error":"wrong request method"})

    if request.method == 'POST':
        try:
            teacher = Teacher.objects.get(id=id)
        except:
            return JsonResponse({"success":False, "error":"no such teacher"})

        teacher.delete()
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


def sp_subject(request, id):
    if request.method == 'GET':
        data = list(Subject.objects.filter(id=id).values())
        if not data:
            return JsonResponse({"success":False, "error":"no such subject"})
        return JsonResponse(data, safe=False)


def sp_subject_delete(request, id):
    if request.method == 'GET':
        return JsonResponse({'saccess':False, "error":"wrong request method"})

    if request.method == 'POST':
        try:
            subject = Subject.objects.get(id=id)
        except:
            return JsonResponse({"success":False, "error":"no such subject"})

        subject.delete()
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


def sp_group(request, id):
    if request.method == 'GET':
        data = list(Group.objects.filter(id=id).values())
        if not data:
            return JsonResponse({"success":False, "error":"no such group"})
        return JsonResponse(data, safe=False)


def sp_group_students(request, id):
    try:
        group = Group.objects.get(id=id)
    except:
        return JsonResponse({"success":False, "error":"no such group"})

    if request.method == 'GET':
        data = list(group.students.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        r = json.loads(request.body)
        try:
            student_id = r['student_id']
        except:
            return JsonResponse({"success":False, "error":"request isn't full"})

        try:
            group.students.get(id=student_id)
            return JsonResponse({"success":False, "error":"student already in group"})
        except:
            group.students.add(student_id)
            group.save()

        return JsonResponse({"success":True})


def sp_group_student_delete(request, group_id, student_id):
    try:
        group = Group.objects.get(id=group_id)
    except:
        return JsonResponse({"success":False, "error":"no such group"})

    if request.method == 'GET':
        return JsonResponse({'saccess':False, "error":"wrong request method"})

    if request.method == 'POST':
        try:
            group.students.remove(Student.objects.get(id=student_id))
        except:
            return JsonResponse({"saccess":False, "error":"student not in group"})

        return JsonResponse({"success":True})


def sp_group_delete(request, id):
    if request.method == 'GET':
        return JsonResponse({'saccess':False, "error":"wrong request method"})

    if request.method == 'POST':
        try:
            group = Group.objects.get(id=id)
        except:
            return JsonResponse({"success":False, "error":"no such group"})

        group.delete()
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
            if r["group"]:
                group = r["group"]
                try:
                    lesson.group = Group.objects.get(id=group)
                except:
                    return JsonResponse({"success":False, "error":"no such group"})
            date = r["date"]
        except KeyError:
            return JsonResponse({"success":False, "error":"request isn't full"})

        try:
            date = datetime(date["year"], date["month"], date["day"], date["hour"], date["minute"])
            lesson.datetime = date
        except:
            return JsonResponse({"success":False, "error":"wrong datetime representation"})

        lesson.save()
        return JsonResponse({"success":True})


def sp_lesson(request, id):
    if request.method == 'GET':
        data = list(Lesson.objects.filter(id=id).values())
        if not data:
            return JsonResponse({"success":False, "error":"no such lesson"})
        return JsonResponse(data, safe=False)


def sp_lesson_visits(request, id):
    try:
        lesson = Lesson.objects.get(id=id)
    except:
        return JsonResponse({"success":False, "error":"no such lesson"})

    if request.method == 'GET':
        data = list(lesson.visits.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        r = json.loads(request.body)
        try:
            student_id = r['student_id']
        except:
            return JsonResponse({"success":False, "error":"request isn't full"})

        try:
            Visit.objects.get(student_id=student_id, lesson_id=id)
            return JsonResponse({"success":False, "error":"visit already exists"})
        except:    
            visit = Visit(student=Student.objects.get(id=student_id),
                        lesson=Lesson.objects.get(id=id))
            visit.save()

        return JsonResponse({"success":True})


def sp_lesson_visit_delete(request, lesson_id, student_id):
    try:
        lesson = Lesson.objects.get(id=lesson_id)
    except:
        return JsonResponse({"success":False, "error":"no such lesson"})

    if request.method == 'GET':
        return JsonResponse({'saccess':False, "error":"wrong request method"})

    if request.method == 'POST':
        try:
            Visit.objects.get(student_id=student_id).delete()
        except:
            return JsonResponse({"saccess":False, "error":"student did not visit lesson"})

        return JsonResponse({"success":True})


def sp_lesson_delete(request, id):
    if request.method == 'GET':
        return JsonResponse({'saccess':False, "error":"wrong request method"})

    if request.method == 'POST':
        try:
            lesson = Lesson.objects.get(id=id)
        except:
            return JsonResponse({"success":False, "error":"no such lesson"})

        lesson.delete()
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


def sp_visit(request, id):
    if request.method == 'GET':
        data = list(Visit.objects.filter(id=id).values())
        if not data:
            return JsonResponse({"success":False, "error":"no such visit"})
        return JsonResponse(data, safe=False)


def sp_visit_delete(request, id):
    if request.method == 'GET':
        return JsonResponse({'saccess':False, "error":"wrong request method"})

    if request.method == 'POST':
        try:
            visit = Visit.objects.get(id=id)
        except:
            return JsonResponse({"success":False, "error":"no such visit"})

        visit.delete()
        return JsonResponse({"success":True})


# SUBSCRIPTION
def subscriptions(request):
    if request.method == 'GET':
        data = list(Subscription.objects.values())
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        r = json.loads(request.body)
        subscription = Subscription()
        try:
            student_id = r['student_id']
            lessons_left = r['lessons']
            duration = r['duration']
        except KeyError:
            return JsonResponse({"success":False, "error":"request isn't full"})

        try:
            student = Student.objects.get(id=student_id)
        except:
            return JsonResponse("success":False, "error":"no such student")

        try:
            year = datetime.today().year + duration['year']
            month = datetime.today().month + duration['month']
            day = datetime.today().day + duration['day']
            last_day = datetime(year=year, month=month, day=day)
        except:
            return JsonResponse("success":False, "error":"wrong duration format")

        subscription.student = student
        subscription.lessons_left = lessons_left
        subscription.last_day = last_day

        return JsonResponse({"success":True})


def sp_subscription(request, id):
    if request.method == 'GET':
        data = list(Group.objects.filter(id=id).values())
        if not data:
            return JsonResponse({"success":False, "error":"no such subscription"})
        return JsonResponse(data, safe=False)



