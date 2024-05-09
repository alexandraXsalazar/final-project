from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Cycle, Pc, Student, Staff, Attendance, StaffFeedback, StuFeedback
from django.contrib.auth import authenticate, login


def index(request):
    return render(request,"index.html")

def login(request):
    if request.method == 'POST':
        # Obtiene los datos del formulario de inicio de sesión
        rolestaff = request.POST.get('loginstaff')
        rolestu = request.POST.get('loginstu')
        usernamestu = request.POST.get('student_logname')
        passwordstu = request.POST.get('student_logpass')
        usernamestaff = request.POST.get('staff_logname')
        passwordstaff = request.POST.get('staff_logpass')
        
        # Autentica al usuario correspondiente según su rol
        if rolestu == "loginstu":
            user = authenticate(username=usernamestu, password=passwordstu)
        elif rolestaff == "loginstaff":
            user = authenticate(username=usernamestaff, password=passwordstaff)
        else:
            return render(request, 'login.html', {'error_message': 'Invalid role'})
        
        print(usernamestu)
        print(passwordstu)
        print(usernamestaff)
        print(passwordstaff)
        print(rolestaff)
        print(rolestu)
        # Verifica si la autenticación fue exitosa
        if user is not None:
            if rolestu == "loginstu":
                print("entro")
                try:
                    usernamestu= Student.objects.get(user=user)
                    login(request, user)
                    return render(request, "layoutstu.html")
                except Student.DoesNotExist:
                    return render(request, 'login.html', {'error_message': 'Invalid student credentials'})
            elif rolestaff == "loginstaff":
                try:
                    usernamestaff = Staff.objects.get(user=user)
                    login(request, user)
                    return render(request, "layoutstaff.html")
                except Staff.DoesNotExist:
                    return render(request, 'login.html', {'error_message': 'Invalid staff credentials'})
        else:
            # La autenticación falló
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # Si no es una solicitud POST, simplemente muestra el formulario de inicio de sesión
        return render(request, 'login.html')