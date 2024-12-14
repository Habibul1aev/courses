

from django.contrib import admin
from django.urls import path, include
from courses import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='home'),
    path('home/', views.main, name='home'),
    path('categories/<int:id>', views.categories, name='categories'),
    path('list/<int:id>', views.list, name='list'), 
    path('statistic/', views.statistic, name='statistic'), 
    path('workspace/', include('workspace.urls')), 

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)