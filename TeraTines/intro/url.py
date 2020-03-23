from django.contrib import admin
from django.urls import path
from intro import views
urlpatterns = [
    path('',views.welcome,name="intro")
]
