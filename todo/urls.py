from django.contrib import admin
from django.urls import path, include
from .views import taskView


urlpatterns = [
    path('', taskView, name="task-view")
]
