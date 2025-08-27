from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('madlib/<int:id>/', views.madlib_form, name='madlib_form'),
    path('about/', views.about, name='about'),
]