from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('aums',views.aums,name="aums"),
    path('attendance',views.attendance,name="attendance"),
    path('grades',views.grades,name="grades"),
    path('marks',views.marks,name="marks"),
    path('tests/<str:sub_code>/',views.tests,name="tests"),
    path('signout',views.signout,name="signout"),
    path('pass_reset',views.pass_reset,name="pass_reset"),
    path('pass_conf',views.pass_conf,name="pass_conf"),
    path('change_pass/<token>/',views.change_pass,name="change_pass"),
    path('profile',views.profile,name="profile"),
]
