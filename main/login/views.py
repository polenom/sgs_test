from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic.edit import BaseFormView, FormMixin, FormView

from login.forms import UserUpdateForm


# Create your views here.

class CheckUser(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("images:list_images")
        else:
            return redirect("login:login_user")


class UserLogin(View):
    class_from = AuthenticationForm
    success_url = reverse_lazy("images:list_images")

    def get(self, request):
        form = self.class_from()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = self.class_from(request, request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect(self.success_url)
        else:
            return render(request, "login.html", {"form": form})


class UserRegistration(CreateView):
    form_class = UserCreationForm
    template_name = "registration.html"
    success_url = reverse_lazy("images:list_images")

    def form_valid(self, form):
        self.object = form.save()
        user = authenticate(
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password1"),
        )
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())


class UserUpdate(LoginRequiredMixin, FormView):
    form_class = UserUpdateForm
    success_url = reverse_lazy("images:list_images")
    template_name = "update_password.html"

    def form_valid(self, form):
        self.request.user.set_password(form.cleaned_data.get("password"))
        self.request.user.save()
        login(self.request, self.request.user)
        return HttpResponseRedirect(self.get_success_url())


class UserLogout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("login:login_user")
