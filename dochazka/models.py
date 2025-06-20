from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

class Department(models.Model):
    name = models.CharField(max_length=32)
    manager = models.ForeignKey('Employee', related_name="departmentManager", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class CustomUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Nebylo zadane uzivatelske jmeno!")

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, username = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)
    
    def create_superuser(self, username = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fields)

class Employee(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    username = models.CharField(max_length=64, default='', unique=True)
    email = models.EmailField(blank=True, default='')
    department = models.ForeignKey('Department', related_name="employees", on_delete=models.CASCADE, null=True, blank=True)
    position = models.CharField(max_length=32)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def get_full_name(self):
        return f"{self.name} {self.surname}"
    
    def get_short_name(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey('Employee', related_name="attendance_records", on_delete=models.CASCADE)
    date = models.DateField()
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True) 

    def __str__(self):
        return f"{self.employee.name} {self.employee.surname} - {self.date} {self.check_in} - {self.check_out}"