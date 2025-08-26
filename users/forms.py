from django import forms
from .models import Student, Teacher, Course, Materials, Grades

class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = [
            'username', 
            'email', 
            'password', 
            'first_name', 
            'last_name', 
            'department', 
            'student_id', 
            'phone',
        ]

class TeacherForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'department',
            'phone',
        ]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name',
            'code',
            'description',
            'department',
            'credits',
            'teacher',
        ]
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = [
            'title',
            'description',
            'file',
            'course',
        ]

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = [
            'student',
            'course',
            'grade',
        ]