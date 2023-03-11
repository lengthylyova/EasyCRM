from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students_all'),
    path('teachers/', views.teachers, name='teachers_all'),
    path('groups/', views.groups, name='groups_all'),
    path('subjects/', views.subjects, name='subjects_all'),
    path('visits/', views.visits, name='visits_all'),
    path('lessons/', views.lessons, name='lessons_all'),
]