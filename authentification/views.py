import email
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

from django.core.mail import send_mail

# Redirection page
from .models import Profile


@csrf_protect
def successful(request):

    return render(request, "registrationSuccessful.html")


# Signup page
@csrf_protect
def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            return redirect("successful")
    else:
        form = UserRegisterForm()

    return render(request, "signup.html", {"form": form})


# Signin page
@csrf_protect
def signin(request):
    error_message = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/profile")
            else:

                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
            error_message = "Invalid username or password."
    form = AuthenticationForm()
    return render(
        request=request,
        template_name="signin.html",
        context={"login_form": form, "error_message": error_message},
    )


def logout(request):
    auth_logout(request)
    return redirect("/authentication/signin")
