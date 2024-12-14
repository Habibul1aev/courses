from django.contrib import admin
from .models import Courses, ImgAttribute, TypeOfCourses, School, TypeOfTraining, Duration, Residence, Category, Retings, Comment
from django.utils.safestring import mark_safe


class Tabular(admin.TabularInline):
    model = ImgAttribute
    extra = 1

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'author','is_publish', 'get_imges')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author')
    readonly_fields = ('id', 'get_full_imges', 'views')
    
    inlines = [Tabular]

    @admin.display(description='Изображение')
    def get_imges(self, course:Courses):
        return mark_safe(f'<img src="{course.photo.url}" width="150px">')

    @admin.display(description='Изображение')
    def get_full_imges(self, course:Courses):
        return mark_safe(f'<img src="{course.photo.url}" width="50%">')
    

@admin.register(ImgAttribute)
class NewImgAttribute(admin.ModelAdmin):
    list_display = ('id', 'product', 'get_img')
    list_display_links = ('id', 'product')

    @admin.display(description='Изображение')
    def get_img(self, img:ImgAttribute):
        return mark_safe(f'<img src="{img.image.url}" width="150px">')
    
@admin.register(Retings)
class RetingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'score',)
    list_display_links = ('id', 'user')
    search_fields = ('user', )
    readonly_fields = ('id', )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'created',)
    list_display_links = ('id', 'user')
    search_fields = ('user', )
    readonly_fields = ('id', )

admin.site.register(Category)
admin.site.register(TypeOfCourses)
admin.site.register(TypeOfTraining)
admin.site.register(School)
admin.site.register(Duration)
admin.site.register(Residence)





