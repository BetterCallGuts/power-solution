from django.urls import path
from . import views

urlpatterns = [
    
    path('',                     views.index,                    name='index')    ,
    path('services/'    ,        views.Service.as_view(),     name='services') ,
    path('generator/',           views.generator,                name='generator'),
    path('UPS/',                 views.UPS,                            name='UPS')      ,
    path('detail/<slug:slug>/',  views.detail,                name='detail')   ,
    path("detail/<slug:slug>/request-info/",   views.,                name='detail')   ,
    path("accessories/",         views.accessories,                  name="accessories"),


]