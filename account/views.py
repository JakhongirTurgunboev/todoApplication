from django.http import HttpResponse
from django.shortcuts import render

from todo.models import Task
#from .forms import NewUserForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from .serializers import TaskSerializer


# Create your views here.

#
# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("/")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="account/register.html", context={"register_form":form})
#
#
# def loginView(request):
# 	if request.method== "POST":
# 		username = request.POST["username"]
# 		password = request.POST["password"]
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			return redirect("/")
# 		else:
# 			return HttpResponse("Ma'lumotni noto'g'ri kiritindingiz")
# 	return render(request, template_name="account/login.html")
#
#
# def logout_view(request):
# 	logout(request)
# 	return redirect("/")


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)