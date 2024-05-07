from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Cycle, Pc, Student, Staff, Attendance, StaffFeedback, StuFeedback
from django.contrib.auth import authenticate, login


def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if user_type == 'student':
            # Authenticate against your custom User model
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to student dashboard or any desired page
            else:
                # Render error.html if authentication fails
                return render(request, 'error.html', {'error_message': 'Invalid username or password.'})

        elif user_type == 'staff':
            # Similarly authenticate staff user
            pass
        else:
            # Render error.html for invalid user type
            return render(request, 'error.html', {'error_message': 'Invalid user type.'})

    return render(request, 'login.html')