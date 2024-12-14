from django.urls import path
from workspace import views

urlpatterns = [
    path('change_profile/', views.change_profile, name='change_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout_prof/', views.logout_prof, name='logout_prof'),
    path('registration/', views.registration_prof, name='registration'),
    path('login/', views.login_prof, name='login'),
    path('create/', views.create, name='create'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('', views.main, name='workspace'),
]