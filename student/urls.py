
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index_page),
    path('view_pdf/', views.view_pdf ,name='view_pdf'),
]