from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students_all'),
    path('students/<int:id>/', views.sp_student, name='specific_student'),
    path('students/delete/<int:id>/', views.sp_student_delete, name='specific_student_delete'),

    path('teachers/', views.teachers, name='teachers_all'),
    path('teachers/<int:id>/', views.sp_teacher, name='specific_teacher'),
    path('teachers/delete/<int:id>/', views.sp_teacher_delete, name='specific_teacher_delete'),

    path('groups/', views.groups, name='groups_all'),
    path('groups/<int:id>/', views.sp_group, name='specific_group'),
    path('groups/delete/<int:id>/', views.sp_group_delete, name='specific_group_delete'),

    path('subjects/', views.subjects, name='subjects_all'),
    path('subjects/<int:id>', views.sp_subject, name='specific_subject'),
    path('subjects/delete/<int:id>', views.sp_subject_delete, name='specific_subject_delete'),

    path('visits/', views.visits, name='visits_all'),
    path('visits/<int:id>/', views.sp_visit, name='specific_visit'),
    path('visits/delete/<int:id>/', views.sp_visit_delete, name='specific_visit_delete'),

    path('lessons/', views.lessons, name='lessons_all'),
    path('lessons/<int:id>', views.sp_lesson, name='specific_lesson'),
    path('lessons/delete/<int:id>', views.sp_lesson_delete, name='specific_lesson_delete'),
]