# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Department, Teacher, Student, Course, Enrollment

# Register your other models as usual
admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)

# Custom admin site for the User model to fix display issue
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        for app in app_list:
            if app['app_label'] == 'users':
                # Move 'User' model to a new 'Authentication and Authorization' group
                auth_model = next(model for model in app['models'] if model['object_name'] == 'User')
                if auth_model:
                    app['models'].remove(auth_model)
                    auth_app = next((app for app in app_list if app['app_label'] == 'auth'), None)
                    if not auth_app:
                        auth_app = {'name': 'Authentication and Authorization', 'app_label': 'auth', 'models': []}
                        app_list.append(auth_app)
                    auth_app['models'].insert(0, auth_model)
        return app_list

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )
    list_display = UserAdmin.list_display + ('role',)

