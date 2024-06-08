from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Define más URLs según sea necesario
]
