from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('list/', views.blogList),
    path('detail/<int:id>', views.blogDetail),
]