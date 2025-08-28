from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Student, Teacher, Course, Materials, Grades
from django.contrib.auth.decorators import login_required
from .decorators import teacher_required, student_required
from .models import Profile
from .forms import StudentForm, TeacherForm, CourseForm, MaterialForm, GradeForm

def home(request):
    return render(request, 'users/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Rolewise redirect
            if user.profile.role == 'student':
                return redirect('student_dashboard')
            elif user.profile.role == 'teacher':
                return redirect('teacher_dashboard')
            elif user.profile.role == 'admin':
                return redirect('admin_dashboard')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')


def student_list(request):
    students = Student.objects.all()   # fetch all students from DB
    return render(request, 'users/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'users/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'users/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":   # confirm delete only on POST
        student.delete()
        return redirect('student_list')
    return render(request, 'users/student_confirm_delete.html', {'student': student})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'users/student_detail.html', {'student': student})

@login_required
@student_required
def view_grades(request):
    grades = Grades.objects.filter(student=request.user.student)
    return render(request, 'users/student_grades.html', {'grades': grades})
@login_required
@student_required
def view_materials(request):
    student_courses = request.user.student.course_set.all()
    materials = Materials.objects.filter(course__in=student_courses)
    return render(request, 'users/student_materials.html', {'materials': materials})



def teacher_list(request):
    teachers = Teacher.objects.all()   # fetch all teachers from DB
    return render(request, 'users/teacher_list.html', {'teachers': teachers})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'users/teacher_form.html', {'form': form})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'users/teacher_form.html', {'form': form})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":   # confirm delete only on POST
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'users/teacher_confirm_delete.html', {'teacher': teacher})


def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'users/teacher_detail.html', {'teacher': teacher})
# Teacher Upload
@login_required
@teacher_required
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_dashboard')
    else:
        form = GradeForm()
    return render(request, 'users/add_grade.html', {'form': form})

@login_required
@teacher_required
def upload_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.uploaded_by = request.user.teacher
            material.save()
            return redirect('teacher_dashboard')
    else:
        form = MaterialForm()
    return render(request, 'users/upload_material.html', {'form': form})

# Student View
@login_required
def student_materials(request):
    materials = Materials.objects.all().order_by('-uploaded_at')
    return render(request, 'users/student_materials.html', {'materials': materials})



def course_list(request):
    courses = Course.objects.all()   # fetch all students from DB
    return render(request, 'users/course_list.html', {'courses': courses})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'users/course_form.html', {'form': form})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'users/course_form.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == "POST":   # confirm delete only on POST
        course.delete()
        return redirect('course_list')
    return render(request, 'users/course_confirm_delete.html', {'course': course})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'users/course_detail.html', {'course': course})
# Dashboards
@login_required
def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'users/teacher_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')
