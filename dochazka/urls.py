from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("employee", views.employee, name="employee"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("attendance", views.attendance, name="attendance")
]