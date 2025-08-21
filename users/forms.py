from django import forms
from .models import Student, Teacher, Course

class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class meta:
        model = Student
        fields = [
            'username', 
            'email', 
            'password', 
            'first_name', 
            'last_name', 
            'department', 
            'student_id', 
            'phone'
        ]
        
class TeacherForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class meta:
        model = Teacher
        fields = [
            'username'
            'email'
            'password'
            'first_name'
            'last_name'
            'department'
            'phone'
        ]

class CourseForm(forms.ModelForm):
    class meta:
        model = Course
        fields = [
            'name'
            'code'
            'description'
            'department'
            'credits'
            'teacher'
        ]

