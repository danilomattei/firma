from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.timezone import now
from .models import Employee, Attendance
from .forms import AttendanceForm
from . formular import *
from django.contrib.auth.forms import *

def index(request):
    return render(request, 'dochazka/layout.html')

def attendance(request):
    attendance = Attendance.objects.all()
    context = {'attendance': attendance}

    return render(request, 'dochazka/attendance.html', context)

def record_attendance(request):
    message = ""
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            passcode = form.cleaned_data['passcode']
            employee = get_object_or_404(Employee, passcode=passcode)
            attendance, created = Attendance.objects.get_or_create(
                employee=employee,
                date=now().date(),
                defaults={'check_in': now().time()}
            )
            if not created:
                attendance.check_out = now().time()
                attendance.save()
                message = "Odchod zaznamenán."
            else:
                message = "Příchod zaznamenán."
    else:
        form = AttendanceForm()

    return render(request, 'dochazka/attendance.html', {'form': form, 'message': message})

def employee(request):
     if not request.user.is_authenticated:
         return HttpResponseRedirect(reverse("login"))
     context = {
         "employee": request.user
     }
     return render(request, "dochazka/employee.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("employee"))
        else:
            return render(request, "dochazka/login.html", {
                "message": "Invalid credentials."
            })
    else:
        return render(request, "dochazka/login.html")

def logout_view(request):
    logout(request)
    return render(request, "dochazka/login.html", {
        "message": "Logged out."
    })

def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            employee = form.save()
            login(request, employee)
            return redirect("/")
    else:
        form = RegistrationForm()
    
    return render(request, "dochazka\sign_up.html", {
        "form":form
        })