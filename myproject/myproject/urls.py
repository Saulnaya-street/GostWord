from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-elements/', views.add_elements, name='add_elements'),
]
