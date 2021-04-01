from django.urls import path
from . import views

app_name = 'icecream'
urlpatterns = [
    path('<int:pk>/', views.detail),
]