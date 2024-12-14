from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from .filter import SearchFilter
from .forms import RetingsForm, CommentForm
from django.core.paginator import Paginator


def main(request):
    courses = Courses.objects.filter(is_publish=True).order_by('-date')
    filter_set = SearchFilter(request.GET, queryset=courses)
    courses = filter_set.qs
    categorys = Category.objects.all()

    min_max = request.GET.get('min_or_max')
    _min = request.GET.get('min')
    _max = request.GET.get('max')

    # if _min is None and _max is None:
    #     _min = 1
    #     _max = 750
    
    # if min_max == '1':
    #     courses = courses.filter(price__gte=int(_min), price__lte=int(_max)).order_by('price')
    # else:
    #     courses = courses.filter(price__gte=int(_min), price__lte=int(_max)).order_by('-price')

    paginator = Paginator(courses, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'body.html' , {'courses': courses, 'filter_set':filter_set, 'min_max':min_max, 'min':_min, 'max':_max, 'page_obj':page_obj,'categorys':categorys})


def categories(request, id):
    category = get_object_or_404(Category, id=id)
    courses = Courses.objects.filter(category=category).filter(is_publish=True).order_by('-date')
    categorys = Category.objects.all()
    filter_set = SearchFilter(request.GET, queryset=courses)
    courses = filter_set.qs

    min_max = request.GET.get('min_or_max')
    _min = request.GET.get('min')
    _max = request.GET.get('max')

    paginator = Paginator(courses, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'school.html', {'courses': courses, 'filter_set':filter_set, 'min_max':min_max, 'min':_min, 'max':_max, 'page_obj':page_obj, 'categorys':categorys})


def list(request, id):
    courses = Courses.objects.get(id=id)
    categorys = Category.objects.all()
    imags = courses.imgs.all()[0:4]
    imags2 = courses.imgs.all()
    courses.views += 1
    courses.save()


    comments = Comment.objects.filter(course=courses)
    form_comment = CommentForm()
    if request.method == 'POST':
        form_comment = CommentForm(data=request.POST)
        if form_comment.is_valid():
            come = form_comment.save(commit=False)
            come.user = request.user
            come.course = courses
            come.save()

    form = RetingsForm()
    if request.method == 'POST':
        form = RetingsForm(data=request.POST)
        if form.is_valid():
            ratings = form.save(commit=False)
            ratings.user = request.user
            ratings.course = courses
            ratings.save()

    courses2 = Courses.objects.filter(id=id)
    filter_set = SearchFilter(request.GET, queryset=courses2)
    courses = filter_set.qs


    return render(request, 'list_courses.html', {'categorys':categorys,'filter_set':filter_set, 'courses':courses, 'imags':imags, 'imags2':imags2, 'form':form, 'form_comment':form_comment, 'comments':comments, 'form':form})


def statistic(request):
    categorys = Category.objects.all()

    return render(request, 'statistic.html', {'categorys':categorys})