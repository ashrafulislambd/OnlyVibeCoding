from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import HttpResponse
from .forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            #form.save()
            messages.success(request, "Successfully created an account")
    else:
        form = SignupForm()
    return render(request, "core/signup.html", { "form" : form })

def login(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            #form.save()
            messages.success(request, "Successfully created an account")
    else:
        form = SignupForm()
    return render(request, "core/signup.html", { "form" : form })

class UserLoginView(LoginView):
    def get_success_url(self):
        return HttpResponse("Success")
    template_name = "core/login.html"