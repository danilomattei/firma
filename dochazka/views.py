from django.shortcuts import render
from .models import Employee
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from .models import Employee, Attendance
from .forms import AttendanceForm

def index(request):
    employees = Employee.objects.all()
    return render(request, 'dochazka/index.html', {'employees': employees})

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