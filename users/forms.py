from django import forms 
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm
from .models import User
from .models import Department, Teacher, Course, Student, Enrollment, User

class UserForm(forms.ModelForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'role',)

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('department_name',)

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('user', 'department')

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'course_description', 'department', 'teacher')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('user', 'department')

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ('student', 'course')

class StudentCreationForm(BaseUserCreationForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select Department")

    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'department',) 

class TeacherCreationForm(BaseUserCreationForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select Department")
    
    class Meta(BaseUserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'department',)