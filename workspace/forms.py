from django import forms
from courses.models import Courses
from django.contrib.auth.forms import UserCreationForm, BaseUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError



class CreateForms(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'photo', 'category', 'description', 'price', 'type_of_training', 'school', 'type_of_courses', 'duration', 'residence', 'is_publish']


        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter the course title',
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'category': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter the description of the course',
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter the price',
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'type_of_training': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'school': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'type_of_courses': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'duration': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'residence': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'is_publish': forms.CheckboxInput(attrs={
                'class': "h-4 w-4 text-blue-500 focus:ring-blue-500"
            }),
        }


class UpdateForms(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'photo', 'category', 'description', 'price', 'type_of_training', 'school', 'type_of_courses', 'duration', 'residence', 'is_publish']


        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter the course title',
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'category': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter the description of the course',
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter the price',
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'type_of_training': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'school': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'type_of_courses': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'duration': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'residence': forms.Select(attrs={
                'class': "w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 mb-3"
            }),
            'is_publish': forms.CheckboxInput(attrs={
                'class': "h-4 w-4 text-blue-500 focus:ring-blue-500"
            }),
        }


class LoginForms(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Введите имя пользователя','class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}))


class RegistrationForm(BaseUserCreationForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    password2 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', 'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}))

    class Meta:
        model = User
        fields = ('username', 'first_name','email', 'password1', 'password2')

        widgets={
            'username': forms.TextInput(attrs={'placeholder': 'Введите ник','class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите имя', 'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'email': forms.EmailInput(attrs={'placeholder':'Введите электронную почту','class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }


class ChangePasswordForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.user: User = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    password_upd1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Введите новый пароль', 'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}))
    password_upd2 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите новый пароль', 'class':'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}))

    def clean(self):
        password1 = self.cleaned_data['password1']
        password_upd1 = self.cleaned_data['password_upd1']
        password_upd2 = self.cleaned_data['password_upd2']
        
        errors = {}

        if not self.user.check_password(password1):
            errors['password1'] = ['Не верный пароль']
        if password_upd1 != password_upd2:
            errors['password_upd2'] = ['Пароль не совподает с преждним']

        if len(errors) > 0:
            raise ValidationError(errors)
        
        return self.cleaned_data
        
class ChangeProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['first_name'].required = True
        self.fields['email'].required = True


    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Введите новый ник','class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите новое имя', 'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'email': forms.EmailInput(attrs={'placeholder':'Введите новую электронную почту','class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
        }
