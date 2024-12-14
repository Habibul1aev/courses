from django.shortcuts import render, redirect
from courses.models import Category, Courses
from courses.filter import SearchFilter
from django.core.paginator import Paginator
from workspace.forms import CreateForms, UpdateForms, RegistrationForm,LoginForms, ChangePasswordForm, ChangeProfileForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .decorators import _login_required, is_owner


@_login_required
def main(request):
    categorys = Category.objects.all()
    page_obj = Courses.objects.filter(author=request.user).order_by('views')
    filter_set = SearchFilter(request.GET, queryset=page_obj)
    page_obj = filter_set.qs

    return render(request, 'workspace/body.html', {'categorys':categorys, 'page_obj':page_obj, 'filter_set':filter_set})

@_login_required
def create(request):
    courses = Courses.objects.all()
    categorys = Category.objects.all()
    if request.method == 'POST':
        form = CreateForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            courses = form.save(commit=False)
            courses.author = request.user
            courses.save()
            messages.success(request, f'Вы создали курс {courses.title}')
            return redirect('/workspace/')
    else:
        form = CreateForms()

    return render(request, 'workspace/create.html', {'categorys':categorys, 'form':form})

@_login_required
@is_owner
def update(request, id):
    courses = Courses.objects.get(id=id)
    categorys = Category.objects.all()

    if request.method == 'POST':
        form = UpdateForms(data=request.POST, files=request.FILES, instance=courses)
        if form.is_valid():
            form.save()
            messages.success(request, f'Вы успешно обновили {courses.category} {courses.title}')
            return redirect('/workspace/')
    else:
        form = UpdateForms(instance=courses)


    return render(request, 'workspace/update.html',  {'categorys':categorys, 'form':form, 'courses':courses})

@_login_required
@is_owner
def delete(request, id):
    courses = Courses.objects.get(id=id)
    name = courses.title
    courses.delete()
    messages.error(request, f'Вы удалили курс {name}')

    return redirect('/workspace/')



def registration_prof(request):
    categorys = Category.objects.all()

    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user1 = form.save()
            login(request, user1)
            messages.success(request, f'Вы успшно создали аккаунт')
            return redirect('/workspace/')

    return render(request, 'auth/register.html', {'form':form, 'categorys':categorys})

def login_prof(request):
    categorys = Category.objects.all()

    form= LoginForms()
    if request.method == 'POST':
        form = LoginForms(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, f'Добро пожаловать {username}')
                return redirect('/workspace/')
            
            messages.error(request, 'Акаунт не найден (')

    return render(request, 'auth/login.html', {'form':form, 'categorys':categorys})

def logout_prof(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/home/')


@_login_required
def change_password(request):
    categorys = Category.objects.all()

    form = ChangePasswordForm()
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            new_pass = form.cleaned_data.get('password_upd1')
            user = request.user
            user.set_password(new_pass)
            user.save()
            login(request, user)
            messages.success(request, f'Успешно изменен пароль {user.username}')

            return redirect('/workspace/')
    print(form.errors)


    return render(request, 'auth/change_password.html', {'form':form, 'categorys':categorys})

@_login_required
def change_profile(request):
    categorys = Category.objects.all()

    form = ChangeProfileForm(instance=request.user)
    if request.method == 'POST':
        form = ChangeProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваш профиль успешно изменен')
            return redirect('/workspace/')

    return render(request, 'auth/change_profile.html', {'form':form, 'categorys':categorys})







