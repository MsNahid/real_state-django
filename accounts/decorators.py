from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('pages:index')
        else:
            return func(request, *args, **kwargs)
    
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return func(request, *args, **kwargs)
            else:
                return redirect('others:notfound')
        return wrapper_func
    
    return decorator