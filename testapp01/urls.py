from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('get-datetime/', views.get_datetime, name='get_datetime'),
    path('add-datetime/', views.add_datetime, name='add_datetime'),
]