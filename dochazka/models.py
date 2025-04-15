from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=32)
    manager = models.ForeignKey('Employee', related_name="departmentManager", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Employee(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    passcode = models.CharField(max_length=7)
    department = models.ForeignKey('Department', related_name="employees", on_delete=models.CASCADE)
    position = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name} {self.surname} - {self.position} in {self.department}"

class Attendance(models.Model):
    employee = models.ForeignKey('Employee', related_name="attendance_records", on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True) 

    def __str__(self):
        return f"{self.employee.name} {self.employee.surname} - {self.date}"