from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Cycle, Pc, Student, Staff, Attendance, StaffFeedback, StuFeedback, User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render(request,"index.html")

@csrf_exempt 
def loginStaff(request):
    if request.method == 'POST':
        # Obtiene los datos del formulario de inicio de sesión
        rolestaff = request.POST.get('lgStaff')
        rolest = request.POST.get('lgStudent')
        usernamestu = request.POST.get('logname')
        passwordstu = request.POST.get('logpass')
        
        # Autentica al usuario correspondiente según su rol
        if rolestaff == "staff": 
            user = authenticate(username=usernamestu, password=passwordstu) # -> esto no esta devolviendo algo
            print(f"hola {user}")
        elif rolest == "student":
            user = authenticate(username=usernamestu, password=passwordstu)  # -> esto no esta devolviendo algo
            print(f"adios {user}")

        else:
            return render(request, 'login.html', {'error_message': 'Invalid role'})
        
        print(user)
        if rolestaff == "staff":
            try:
                usernamestaff = Staff.objects.get(user_id=3) 
                return render(request, "index.html")
            except Staff.DoesNotExist:
                return render(request, 'login.html', {'error_message': 'Invalid staff credentials'})
        elif rolest == "student":
            try:
                usernamestudent = Student.objects.get(user_id=3)
                return render(request, "index.html")
            except Student.DoesNotExist:
                return render(request, 'login.html', {'error_message ': 'Invalid student credentials'})
            
       
        return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        # Si no es una solicitud POST, simplemente muestra el formulario de inicio de sesión
        return render(request, 'login.html')