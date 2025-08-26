from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('students/', views.student_list, name='student_list'),  # Students list
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/grades/', views.view_grades, name='view_grades'),
    path('students/materials/', views.view_materials, name='view_materials'),

    path('teachers/', views.teacher_list, name='teacher_list'),  # Teachers list
    path('teachers/create/', views.teacher_create, name='teacher_create'),
    path('teachers/<int:pk>/update/', views.teacher_update, name='teacher_update'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('teachers/add-grade/', views.add_grade, name='add_grade'),
    path('teachers/upload-material/', views.upload_material, name='upload_material'),
    
    path('courses/', views.course_list, name='course_list'), # Courses list
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/<int:pk>/update/', views.course_update, name='course_update'),
    path('courses/<int:pk>/delete/', views.course_delete, name='course_delete'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

