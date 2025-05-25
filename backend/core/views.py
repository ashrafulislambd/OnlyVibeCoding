from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from .forms import SignupForm
from .models import Profile
from .config import university_mappings

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = user.email
            for key in university_mappings:
                if email.endswith(university_mappings[key][0]):
                    university = university_mappings[key][1]
            profile = Profile(university=university)
            profile.user = user
            profile.save()
            messages.success(request, "Successfully created an account")
            return redirect("/login")
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
        return reverse("profile")
    template_name = "core/login.html"

class ProfileDetails(DetailView, LoginRequiredMixin):
    model = Profile
    context_object_name = "profile"
    template_name = "core/profile.html" 

    def get_object(self, queryset = None):
        return self.request.user.profile
    
class EditProfile(UpdateView, LoginRequiredMixin):
    model = Profile
    fields = ['department', 'program', 'year_of_study']
    success_url = '/profile'
    template_name = "core/edit_profile.html"

    def get_object(self, queryset = None):
        return self.request.user.profile
    


