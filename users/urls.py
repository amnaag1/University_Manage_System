from django.urls import path
from . import views

urlpatterns = [
    # Home url
    path('', views.home, name='home'),

    # Department URls
    path('departments/<pk>/', views.department_detail, name='department_detail'),
    path('departments/create', views.department_create, name='department_create'),
    path('departments/<pk>/update', views.department_update, name='department_create'),
    path('departments/<pk>/delete', views.department_delete, name='department_delete'),
    # Teacher urls
    path('teachers/<int:id>', views.teacher_detail, name='teacher_detail'),
    path('teachers/create', views.teacher_create, name='teacher_create'),
    path('teachers/<pk>/update', views.teacher_update, name='teacher_update'),
    path('teachers/<pk>/delete', views.teacher_delete, name='teacher_delete'),
    # COurse urls
    path('courses/<int:id>', views.course_detail, name='course_detail'),
    path('courses/create', views.course_create, name='course_create'),
    path('courses/<pk>/update', views.course_update, name='course_update'),
    path('courses/<pk>/delete', views.course_delete, name='course_delete'),
    # Student urls
    path('students/<int:id>', views.student_detail, name='student_detail'),
    path('students/create', views.student_create, name='student_create'),
    path('students/<pk>/update', views.student_update, name='student_update'),
    path('students/<pk>/delete', views.student_delete, name='student_delete'),
    # Enrollment urls
    path('enrollments/<int:id>', views.enrollment_detail, name='enrollment_detail'),
    path('enrollments/create', views.enrollment_create, name='enrollment_create'),
    path('enrollments/<pk>/update', views.enrollment_update, name='enrollment_update'),
    path('enrollments/<pk>/delete', views.enrollment_delete, name='enrollment_delete'),
    # Authentication urls
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    # Dashboard Urls
    path('dashboard/', views.dashboard, name='dashboard'),

    # Admin-dashboard urls
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/manage-students/', views.manage_students, name='manage_students'),
    path('admin/manage-teachers/', views.manage_teachers, name='manage_teachers'),
    path('admin/manage-attendance/', views.manage_attendance_admin, name='manage_attendance_admin'),
    path('admin/manage-enrollment/', views.manage_enrollment_admin, name='manage_enrollment_admin'),
    path('admin/add-enrollment/', views.add_enrollment_admin, name='add_enrollment_admin'),
    path('admin/manage-students/<int:id>/', views.view_student_details, name='view_student_details'),
    path('admin/manage-students/add/', views.add_student_admin, name='add_student_admin'),
    path('admin/manage-teachers/<int:id>/', views.view_teacher_details, name='view_teacher_details'),
    path('admin/manage-teachers/add/', views.add_teacher_admin, name='add_teacher_admin'),
    path('admin/enrollment/<int:pk>/edit/', views.edit_enrollment, name='edit_enrollment'),
    path('admin/enrollment/<int:pk>/delete/', views.delete_enrollment, name='delete_enrollment'),
    path('admin/manage-courses/', views.manage_courses_admin, name='manage_courses_admin'),
    path('admin/manage-courses/<int:course_id>/', views.course_detail_admin, name='course_detail_admin'),
    

    # Teacher-dashboard urls
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/manage-courses/', views.manage_courses, name='manage_courses'),
    path('teacher/manage-grades/<int:course_id>/', views.manage_grades, name='manage_grades'),
    path('teacher/manage-attendance/<int:course_id>/', views.manage_attendance, name='manage_attendance'),

    # Student-dashboard urls
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/my-courses/', views.my_courses, name='my_courses'),
    path('student/my-grades/', views.my_grades, name='my_grades'),
    path('student/my-attendance/', views.my_attendance, name='my_attendance'),



]