from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name  = "index"),
    path("login", views.loginStaff, name="loginStaff"),
    path("logout", views.logout_view, name="logout"),
    path("staffinfo", views.staffinfo, name="staffinfo"),
    path("game_view", views.game_view, name="game_view"),
]
