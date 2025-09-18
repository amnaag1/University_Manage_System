from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.forms import modelformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Student, Department, Teacher, Course, Enrollment, Grade, Attendance
from .forms import DepartmentForm, TeacherForm, StudentForm, CourseForm, EnrollmentForm, UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Count, Q
from collections import defaultdict
from .forms import StudentCreationForm, TeacherCreationForm
import datetime  


def home(request):
    return render(request, 'home.html')

# Department views
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def department_detail(request, pk):
    department = Department.objects.get(pk=pk)
    return render(request, 'department_detail.html', {'department': department})

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'department_form.html', {'form': form})

def department_update(request, pk):
    department = Department.objects.get(pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'department_form.html', {'form': form})

def department_delete(request, pk):
    department = Department.objects.get(pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'department_confirm_delete.html', {'department': department})
      
# Teacher Views
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return render(request, 'teacher_detail.html', {'teacher': teacher})

def teacher_create(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        teacher_form = TeacherForm(request.POST)

        if user_form.is_valid() and teacher_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.role = 'Teacher' 
            new_user.save()

            new_teacher = teacher_form.save(commit=False)
            new_teacher.user = new_user 
            new_teacher.save()

            return redirect('teacher_list')
    else:
        user_form = UserForm()
        teacher_form = TeacherForm()
    
    return render(request, 'teacher_form.html', {'user_form': user_form, 'teacher_form': teacher_form})

def teacher_update(request, pk):
    teacher = Teacher.objects.get(pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
        else:
            form = TeacherForm(instance=teacher)
        return render(request, 'teacher_form.html', {'form': form})
    
def teacher_delete(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'teahcer_confirm_delete.html', {'teacher': teacher})

# Course Views
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course_detail.html', {'course': course})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
        else:
            form = CourseForm()
    return render(request, 'course_form.html', {'form': form})

def course_update(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
        else:
            form = CourseForm(instance=course)
        return render(request, 'course_form.html', {'form': form})
    
def course_delete(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course_confirm_delete.html', {'course': course})

# Student Views
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.all(pk=pk)
    return render(request, 'student_detail.html', {'student': student})

def student_create(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.role = 'student' 
            new_user.save()

            new_student = student_form.save(commit=False)
            new_student.user = new_user 
            new_student.save()

            return redirect('student_list')
    else:
        user_form = UserForm()
        student_form = StudentForm()
    
    return render(request, 'student_form.html', {'user_form': user_form, 'student_form': student_form})

def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.PSOT)
        if form.is_valid():
            form.save()
            return render('student_list')
            
        else:
            form = StudentForm(instance=student)
        return render(request, 'student_form.html', {'form': form})
    
def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})

# Enrollment Views
def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment_list.html', {'enrollments': enrollments})

def enrollment_detail(request, pk):
    enrollment = Enrollment.objects.get(pk=pk)
    return render(request, 'enrollment_detail.html', {'enrollment': enrollment})

def enrollment_create(request):
    if request.method == 'POST':
        form - EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollment_form.html', {'form':form})

def enrollment_update(request, pk):
    enrollment = Enrollment.objects.get(pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
        else:
            form = EnrollmentForm(instance=enrollment)
        return render(request, 'enrollment_form.html', {'form':form})
    
def enrollment_delete(request, pk):
    enrollment = Enrollment.objects.get(pk=pk)
    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')
    return render(request, 'enrollment_confirm_delete.html', {'enrollment':enrollment})

# Register View
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.role = user_form.cleaned_data.get('role')
            user.save()

            if user.role == 'Teacher':
                Teacher.objects.create(user=user, department=Department.objects.first()) 
            elif user.role == 'Student':
                Student.objects.create(user=user, department=Department.objects.first()) 
            
            login(request, user)
            return redirect('dashboard')
    else:
        user_form = UserForm()
    
    return render(request, 'registration/register.html', {'user_form': user_form})
    
# login_user view
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                
                # Redirect based on user role
                if user.role == 'Admin':
                    return redirect('admin_dashboard')
                elif user.role == 'Teacher':
                    return redirect('teacher_dashboard')
                elif user.role == 'Student':
                    return redirect('student_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

# logout_user view
def logout_user(request):
    logout(request)
    # messages.info(request, "You have been logged out successfully.")
    return redirect('login_user')

# Dashboards
# Admin Dashboard
# def is_admin(user):
#     return user.is_superuser

# @user_passes_test(is_admin)
@login_required
def admin_dashboard(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_courses = Course.objects.count()

    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_courses': total_courses
    }
    return render(request, 'dashboard/admin_dashboard.html', context)

@login_required
def manage_students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'admin/manage_students.html', context)

@login_required
def manage_teachers(request):
    teachers = Teacher.objects.all()
    context = {'teachers': teachers}
    return render(request, 'admin/manage_teachers.html', context)

@login_required
def manage_attendance_admin(request):
    all_attendance = Attendance.objects.all().select_related('student__user', 'course')

    context = {
        'all_attendance': all_attendance
    }
    return render(request, 'admin/manage_attendance_admin.html', context)

@login_required
def manage_enrollment_admin(request):
    enrollments = Enrollment.objects.all().order_by('student__user__username')
    
    context = {'enrollments': enrollments}
    return render(request, 'admin/manage_enrollment_admin.html', context)

@login_required
def add_enrollment_admin(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enrollment added successfully!')
            return redirect('manage_enrollment_admin')
    else:
        form = EnrollmentForm()
    
    context = {'form': form}
    return render(request, 'admin/add_enrollment_admin.html', context)

@login_required
def view_student_details(request, id):
    try:
        student = Student.objects.get(id=id)
        # Fetch courses the student is enrolled in
        enrolled_courses = Enrollment.objects.filter(student=student)
        context = {
            'student': student,
            'enrolled_courses': enrolled_courses
        }
        return render(request, 'admin/view_student_details.html', context)
    except Student.DoesNotExist:
        messages.error(request, 'Student not found.')
        return redirect('manage_students')
    
@login_required
def add_student_admin(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            # Create the user first
            user = form.save(commit=False)
            user.role = 'Student'
            user.save()

            # Get the department from the form
            department = form.cleaned_data['department']

            # create the student object with the user and department
            Student.objects.create(user=user, department=department)
            
            messages.success(request, 'Student added successfully.')
            return redirect('manage_students')
    else:
        form = StudentCreationForm()
    
    context = {'form': form, 'page_title': 'Add New Student'}
    return render(request, 'admin/add_user.html', context)

@login_required
def view_teacher_details(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
        # Fetch courses the teacher is assigned to
        taught_courses = Course.objects.filter(teacher=teacher)
        context = {
            'teacher': teacher,
            'taught_courses': taught_courses
        }
        return render(request, 'admin/view_teacher_details.html', context)
    except Teacher.DoesNotExist:
        messages.error(request, 'Teacher not found.')
        return redirect('manage_teachers')
    
@login_required
def add_teacher_admin(request):
    if request.method == 'POST':
        form = TeacherCreationForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'Teacher'
            user.save()
            department = form.cleaned_data['department'] 
            Teacher.objects.create(user=user, department=department) 
            
            messages.success(request, 'Teacher added successfully.')
            return redirect('manage_teachers')
    else:
        form = TeacherCreationForm()
    
    context = {'form': form, 'page_title': 'Add New Teacher'}
    return render(request, 'admin/add_user.html', context)
    
@login_required
def edit_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enrollment updated successfully!')
            return redirect('manage_enrollment_admin')
    else:
        form = EnrollmentForm(instance=enrollment)
    
    context = {'form': form}
    return render(request, 'admin/edit_enrollment.html', context)

@login_required
def delete_enrollment(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Enrollment deleted successfully!')
        return redirect('manage_enrollment_admin')
    
    context = {'enrollment': enrollment}
    return render(request, 'admin/confirm_delete_enrollment.html', context)

@login_required
def manage_courses_admin(request):
    courses = Course.objects.all().select_related('teacher')
    context = {
        'courses': courses
    }
    return render(request, 'admin/manage_courses.html', context)

@login_required
def course_detail_admin(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    enrolled_students = Enrollment.objects.filter(course=course).select_related('student__user')
    
    # Get all students and teachers to show in the dropdowns for selection
    all_students = Student.objects.all().select_related('user')
    all_teachers = Teacher.objects.all().select_related('user')

    if request.method == 'POST':
        new_teacher_id = request.POST.get('teacher_id')
        if new_teacher_id:
            try:
                new_teacher = Teacher.objects.get(pk=new_teacher_id)
                course.teacher = new_teacher
                course.save()
                messages.success(request, f'Teacher for {course.course_name} updated successfully.')
            except Teacher.DoesNotExist:
                messages.error(request, 'Selected teacher does not exist.')
        else:
            course.teacher = None
            course.save()
            messages.info(request, f'Teacher for {course.course_name} has been unassigned.')
            
        # for the Student ID 
        student_ids_to_enroll = request.POST.getlist('enroll_student')
        
        # Check if the list of student IDs is not empty
        if student_ids_to_enroll:
            Enrollment.objects.filter(course=course).delete()
            for student_id in student_ids_to_enroll:
                # Add a check to ensure the ID is not an empty string
                if student_id:
                    student = get_object_or_404(Student, pk=student_id)
                    Enrollment.objects.create(student=student, course=course)
            messages.success(request, f'Student enrollments for {course.course_name} updated successfully.')
        else:
            # If no students are selected, delete all enrollments for this course
            Enrollment.objects.filter(course=course).delete()
            messages.info(request, f'All student enrollments for {course.course_name} have been removed.')

        return redirect('course_detail_admin', course_id=course.id)

    context = {
        'course': course,
        'enrolled_students': enrolled_students,
        'all_students': all_students,
        'all_teachers': all_teachers,
    }
    return render(request, 'admin/course_detail_admin.html', context)







# Teacher Dashboard
@login_required
def teacher_dashboard(request):
    if request.user.role != 'Teacher':
        return redirect('dashboard')
    
    teacher = get_object_or_404(Teacher, user=request.user)
    courses = Course.objects.filter(teacher=teacher) 
    enrolled_students_count = Enrollment.objects.filter(course__in=courses).values('student').annotate(count=Count('student', distinct=True)).count()
    
    context = {
        'teacher': teacher,
        'courses': courses,
        'total_students': enrolled_students_count,
    }
    return render(request, 'dashboard/teacher_dashboard.html', context)
    
@login_required
def manage_courses(request):
    if request.user.role != 'Teacher':
        return redirect('dashboard')
    
    teacher = Teacher.objects.get(user=request.user)
    courses = Course.objects.filter(teacher=teacher)
    
    context = {
        'courses': courses,
    }
    return render(request, 'teacher/manage_courses.html', context)


@login_required
def manage_grades(request, course_id):
    if request.user.role != 'Teacher':
        return redirect('dashboard')
    
    teacher = get_object_or_404(Teacher, user=request.user)
    course = get_object_or_404(Course, id=course_id, teacher=teacher)
    enrolled_students = Student.objects.filter(enrollment__course=course)
    
    # Get grade object
    for student in enrolled_students:
        Grade.objects.get_or_create(
            student=student, 
            course=course, 
            defaults={'marks': 0, 'score': 0.00}
        )
    
    grades = Grade.objects.filter(course=course)
    
    GradeFormSet = modelformset_factory(Grade, fields=('score',), extra=0)
    
    if request.method == 'POST':
        formset = GradeFormSet(request.POST, queryset=grades)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Grades updated successfully!')
            return redirect('manage_grades', course_id=course.id)
    else:
        formset = GradeFormSet(queryset=grades)
    
    # Prepare the context to display student names alongside the grade form
    forms_and_grades = zip(formset, grades)
    
    context = {
        'course': course,
        'forms_and_grades': forms_and_grades,
        'formset': formset,
    }
    return render(request, 'teacher/manage_grades.html', context)

@login_required
def manage_attendance(request, course_id):
    if request.user.role != 'Teacher':
        return redirect('dashboard')
    
    teacher = get_object_or_404(Teacher, user=request.user)
    course = get_object_or_404(Course, id=course_id, teacher=teacher)
    
    # Get all enrollments for this specific course
    enrollments = Enrollment.objects.filter(course=course).select_related('student')
    
    # Check if a date is provided, otherwise use today's date
    date_str = request.GET.get('date', datetime.date.today().strftime('%Y-%m-%d'))
    attendance_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    
    # Create or update attendance records for each student
    for enrollment in enrollments:
        Attendance.objects.get_or_create(
            student=enrollment.student, 
            course=course,
            teacher=teacher,
            date=attendance_date,
            defaults={'status': 'A'} # Default to Absent if not marked
        )
    
    # Fetch all attendance records for the course on the selected date
    attendance_records = Attendance.objects.filter(course=course, date=attendance_date).select_related('student__user')
    
    # Create a list to hold the combined data
    attendance_data = []
    for record in attendance_records:
        attendance_data.append({
            'student_name': record.student.user.username,
            'course_name': record.course.course_name,
            'status': record.status,
            'record_id': record.id, # ID requeired for attendance
        })

    context = {
        'course': course,
        'attendance_data': attendance_data,
        'attendance_date': attendance_date,
    }

    if request.method == 'POST':
        for record in attendance_records:
            # Get the status from the form data
            status = request.POST.get(f"status_{record.id}")
            if status:
                record.status = status
                record.save()
        messages.success(request, "Attendance updated successfully!")
        return redirect('manage_attendance', course_id=course.id)

    return render(request, 'teacher/manage_attendance.html', context)




# Student Dashboard

@login_required
def student_dashboard(request):
    if request.user.role != 'Student':
        return redirect('dashboard')
    
    student = get_object_or_404(Student, user=request.user)

    # Fetch courses, grades, and attendance
    enrollments = Enrollment.objects.filter(student=student).select_related('course')
    grades = Grade.objects.filter(student=student).select_related('course')
    attendance_records = Attendance.objects.filter(student=student).select_related('course')

    # Calculate attendance percentage for each course
    attendance_summary = {}
    course_attendance_counts = defaultdict(lambda: {'total': 0, 'present': 0})

    for record in attendance_records:
        course_id = record.course.id
        course_attendance_counts[course_id]['total'] += 1
        if record.status == 'P':
            course_attendance_counts[course_id]['present'] += 1

    for course_id, counts in course_attendance_counts.items():
        total_classes = counts['total']
        present_classes = counts['present']
        
        if total_classes > 0:
            percentage = (present_classes / total_classes) * 100
            attendance_summary[course_id] = {
                'percentage': round(percentage, 2),
                'total_classes': total_classes,
                'present_classes': present_classes,
            }
        else:
            attendance_summary[course_id] = {
                'percentage': 0,
                'total_classes': 0,
                'present_classes': 0,
            }
    
    context = {
        'enrollments': enrollments,
        'grades': grades,
        'attendance_summary': attendance_summary,
    }
    return render(request, 'dashboard/student_dashboard.html', context)

@login_required
def my_courses(request):
    if request.user.role != 'Student':
        return redirect('dashboard')
    
    student = get_object_or_404(Student, user=request.user)
    
    # Get all enrollments for this specific student
    enrollments = Enrollment.objects.filter(student=student).select_related('course')
    
    context = {
        'enrollments': enrollments,
    }
    
    return render(request, 'student/my_courses.html', context)


@login_required
def my_grades(request):
    if request.user.role != 'Student':
        return redirect('dashboard')

    student = get_object_or_404(Student, user=request.user)
    
    # Get all grades for this specific student, pre-fetching the related course
    grades = Grade.objects.filter(student=student).select_related('course')
    
    context = {
        'grades': grades,
    }
    
    return render(request, 'student/my_grades.html', context)

@login_required
def my_attendance(request):
    if request.user.role != 'Student':
        return redirect('dashboard')
    
    student = get_object_or_404(Student, user=request.user)
    
    # Get attendance records for the student
    attendance_records = Attendance.objects.filter(student=student).select_related('course')
    
    context = {
        'attendance_records': attendance_records,
    }
    
    return render(request, 'student/my_attendance.html', context)




@login_required
def dashboard(request):
    if request.user.role == 'Admin':
        return redirect('admin_dashboard')
    elif request.user.role == 'Teacher':
        return redirect('teacher_dashboard')
    elif request.user.role == 'Student':
        return redirect('student_dashboard')

    return redirect('login_user')



        
