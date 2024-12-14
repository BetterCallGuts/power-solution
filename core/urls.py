from django.urls import path
from . import views

urlpatterns = [


    path('',                                       views.index.as_view(),                                             name='index')    ,
    path('services/'    ,                          views.Service.as_view(),                                          name='services') ,

    path('generator/ferbo/',                       views.FerboView.as_view(),                name='generator-ferbo'),
    path('generator/po-so/',                       views.generator,                                            name='generator-poso'),
    path('generator/po-so/<slug:slug>/',           views.FerboDetailView.as_view(),                name='generator-poso-details'), 

    path('UPS/',                                views.UPS.as_view(),                                              name='UPS')      ,
    path('detail/<slug:slug>/',                 views.DetailView.as_view(),                                     name='detail')   ,
    path("detail/<slug:slug>/request-info/",    views.RequestInfoView.as_view() ,                   name='request-info')   ,
    path("accessories/ups/",                        views.accessories_ups.as_view(),                                      name="accessories-ups"),  

    path("accessories/",                        views.accessories_generator.as_view(),                                      name="accessories-generator"),  


]