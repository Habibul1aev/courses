import django_filters
from django import forms
from .models import Courses, TypeOfTraining, School, TypeOfCourses, Duration, Residence
 
class SearchFilter(django_filters.FilterSet):
    type_of_training = django_filters.ChoiceFilter(
        choices=[(i.id, i.title) for i in TypeOfTraining.objects.all()],
        empty_label='Выбрать',  
        widget=forms.Select(attrs={'class': 'custom-select'})
    )
    
    school = django_filters.ChoiceFilter(
        choices=[(i.id, i.title) for i in School.objects.all()],
        empty_label='Выбрать',  
        widget=forms.Select(attrs={'class': 'custom-select'})
    )
    
    
    type_of_courses = django_filters.ChoiceFilter(
        choices=[(i.id, i.title) for i in TypeOfCourses.objects.all()],
        empty_label='Выбрать',  
        widget=forms.Select(attrs={'class': 'custom-select'}),
        
    )
    
    
    duration = django_filters.ChoiceFilter(
        choices=[(i.id, i.title) for i in Duration.objects.all()],
        empty_label='Выбрать',  
        widget=forms.Select(attrs={'class': 'custom-select'})
    )
    
    residence = django_filters.ChoiceFilter(
        choices=[(i.id, i.title) for i in Residence.objects.all()],
        empty_label='Выбрать',  
        widget=forms.Select(attrs={'class': 'custom-select'})
    )

    class Meta:
        model = Courses
        fields = ('type_of_training', 'school', 'type_of_courses', 'duration', 'residence')



# class PriceFilter(django_filters.FilterSet):
#     min_or_max = django_filters.ChoiceFilter(
#         choices = [('min', 'От низкой к высокой цене'), ('max', 'От высокой к низкой цене')],
#         empty_label=None,
#         label = 'Сортировка'
#     )

#     # price = django_filters.NumberFilter()
#     price_gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
#     price_lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
