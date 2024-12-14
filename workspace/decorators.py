from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from courses.models import Courses


def _login_required(func):
    def inner(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, 'You are not authenticated')
            return redirect('/workspace/registration')
        
        return func(request, *args, **kwargs)

    return inner


def is_owner(view_func):

    def inner(request, id, *args, **kwargs):

        courses = get_object_or_404(Courses, id=int(id))

        if courses.author != request.user:
            messages.warning(request, 'You are not the owner of this courses')
            return redirect('/workspace/')

        return view_func(request, id, *args, **kwargs)

    return inner