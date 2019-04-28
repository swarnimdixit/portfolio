from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogpost, name='blog'),
    path('<int:blog_id>', views.blogdetail, name='detail')
]