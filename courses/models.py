from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User

class Courses(models.Model):
    title = models.CharField('Название', max_length=30)
    photo = models.ImageField('Фото', upload_to='imgs/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='courses', verbose_name='Категория')
    description = models.TextField('Описание', max_length=120)
    price = models.IntegerField('Цена')
    type_of_training = models.ForeignKey('TypeOfTraining', on_delete=models.PROTECT, related_name='courses', verbose_name='Тип обучения')
    school = models.ForeignKey('School', on_delete=models.PROTECT, related_name='courses', verbose_name='Школа')
    type_of_courses = models.ForeignKey('TypeOfCourses', on_delete=models.PROTECT, related_name='courses', verbose_name='Тип курса')
    duration = models.ForeignKey('Duration', on_delete=models.PROTECT, related_name='courses', verbose_name='Продолжитeльность')
    residence = models.ForeignKey('Residence', on_delete=models.PROTECT, related_name='courses', verbose_name='Проживание')
    date = models.DateField('Дата добовения', auto_now_add=True)
    is_publish = models.BooleanField('Публичность', default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    views = models.PositiveIntegerField('Просмотры', default=0)

    def __str__(self):
        return f'{self.title}'
    
    def averge_retings(self):
        ratings = self.retings.all()
        if ratings:
            return sum([rating.score for rating in ratings]) / len(ratings)
        return 0
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Courses', on_delete=models.CASCADE)
    text = models.TextField('Текстовый комментарий', max_length=500)
    created = models.DateTimeField('Добавлен', auto_now_add=True)
    moder = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user}  {self.course}'
    
class Retings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Courses', related_name='retings', on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    def __str__(self):
        return f"{self.score} by {self.user.username} for {self.course.title}"
    
class Category(models.Model):
    title = models.CharField('Категория', max_length=20)
    def __str__(self):
        return f'{self.title}'
    
class ImgAttribute(models.Model):
    product = models.ForeignKey('Courses', on_delete=models.CASCADE, related_name='imgs', verbose_name='Связь')
    image = ResizedImageField('изображение', upload_to='product_images/')
    def __str__(self) -> str:
        return f'{self.product}'
    
class TypeOfTraining(models.Model):
    title = models.CharField('Название', max_length=10)

    def __str__(self) -> str:
        return f'{self.title}'
    

class School(models.Model):
    title = models.CharField('Название', max_length=10)

    def __str__(self) -> str:
        return f'{self.title}'
    

class TypeOfCourses(models.Model):
    title = models.CharField('Название', max_length=10)

    def __str__(self) -> str:
        return f'{self.title}'
    

class Duration(models.Model):
    title = models.CharField('Название', max_length=10)

    def __str__(self) -> str:
        return f'{self.title}'
    
class Residence(models.Model):
    title = models.CharField('Название', max_length=10)

    def __str__(self) -> str:
        return f'{self.title}'
    



