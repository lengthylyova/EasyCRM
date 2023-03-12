from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students_all'),
    path('students/<int:id>/', views.sp_student, name='specific_student'),
    path('students/<int:id>/visits/', views.sp_student_visits, name='specific_student_visits'),
    path('students/<int:id>/groups/', views.sp_student_groups, name='specific_student_groups'),
    path('students/delete/<int:id>/', views.sp_student_delete, name='specific_student_delete'),

    path('teachers/', views.teachers, name='teachers_all'),
    path('teachers/<int:id>/', views.sp_teacher, name='specific_teacher'),
    path('teachers/<int:id>/groups/', views.sp_teacher_groups, name='specific_group_students'),
    path('teachers/delete/<int:id>/', views.sp_teacher_delete, name='specific_teacher_delete'),

    path('groups/', views.groups, name='groups_all'),
    path('groups/<int:id>/', views.sp_group, name='specific_group'),
    path('groups/<int:id>/students', views.sp_group_students, name='specific_group_students'),
    path('groups/delete/<int:id>/', views.sp_group_delete, name='specific_group_delete'),

    path('subjects/', views.subjects, name='subjects_all'),
    path('subjects/<int:id>/', views.sp_subject, name='specific_subject'),
    path('subjects/delete/<int:id>', views.sp_subject_delete, name='specific_subject_delete'),

    path('visits/', views.visits, name='visits_all'),
    path('visits/<int:id>/', views.sp_visit, name='specific_visit'),
    path('visits/delete/<int:id>/', views.sp_visit_delete, name='specific_visit_delete'),

    path('lessons/', views.lessons, name='lessons_all'),
    path('lessons/<int:id>/', views.sp_lesson, name='specific_lesson'),
    path('lessons/<int:id>/visits/', views.sp_lesson_visits, name='specific_lesson_visits'),
    path('lessons/delete/<int:id>/', views.sp_lesson_delete, name='specific_lesson_delete'),
]
