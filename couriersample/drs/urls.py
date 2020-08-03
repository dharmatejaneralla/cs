from django.urls import path
from . import views

urlpatterns=[
    path('/', views.drs_index),
    path('/drs_generate',views.generate_drs),
    path('/display_drs',views.display_drs)
]
