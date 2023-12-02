from django.contrib import admin
from django.urls import path

from basic_layout import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index , name='index'),
    path('about/', views.about , name='about'),
    path('recipe/', views.recipe , name='recipe'),
    path('contact/' , views.contact , name='contact'),
    path('blog/' , views.blog , name='blog'),
]
