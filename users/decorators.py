from django.shortcuts import redirect
from functools import wraps

def teacher_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'teacher'):
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper

def student_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'student'):
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper
