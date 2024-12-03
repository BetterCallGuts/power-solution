from django.urls import path
from . import views

urlpatterns = [
    
    path('',                 views.index,     name='index'),
    path('about/'    ,       views.about,     name='about'),
    path('generator/',       views.generator, name='generator'),
    path('detail/<str:id>/', views.detail, name='detail'),
]