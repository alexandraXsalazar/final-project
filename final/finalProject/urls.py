from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name  = "index"),
    path("login", views.loginStaff, name="loginStaff"),
    path("logout", views.logout_view, name="logout"),
    path("staffinfo", views.staffinfo, name="staffinfo"),
    path("studentinfo", views.studentinfo, name="studentinfo"),
    path("game_view", views.game_view, name="game_view"),
    path("duckBot", views.duckBot, name="duckBot"),
    path('chat/', views.chatbot_response, name='chatbot_response'),
    path('takeAtt/', views.takeAtt, name='takeAtt'),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path('network/', views.network, name='network'),
    path("new_post", views.new_post, name="new_post"), 
    path('layoutstu/', views.layoutstu, name='layoutstu'),
    path('layoutstaff/', views.layoutstaff, name='layoutstaff'),
    
]
