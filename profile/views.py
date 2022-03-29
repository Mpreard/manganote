from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Home page
from authentification.models import Profile
from profile.forms import UpdateUserForm


@csrf_protect
@login_required(login_url="/authentification/signin")
def homeUsers(request):
    profile = Profile.objects.filter(user_id=request.user.id)
    if profile:
        context = {
            "telephone": profile.first().phoneNumber,
        }
    else:
        context = {}

    return render(request, "home.html", context)


@csrf_protect
@login_required(login_url="/authentication/signin")
def edit(request):
    User = get_user_model()
    user = User.objects.filter(id=request.user.id)
    profile = Profile.objects.filter(user_id=request.user.id)
    form = UpdateUserForm(request.POST)

    if request.method == "POST":
        if len(form.errors) == 0:
            body_unicode = request.POST
            user.update(
                first_name=body_unicode["first_name"],
                last_name=body_unicode["last_name"],
            )

            profile.update(phoneNumber=body_unicode["telephone"], picture=None)

            if len(form["password"].value()) != 0:
                usr = User.objects.get(id=request.user.id)
                usr.set_password(body_unicode["password"])
                usr.save()

            context = {
                "form": form,
            }

            return redirect("view-profile")

        else:
            form = UpdateUserForm(request.POST)
            context = {
                "form": form,
            }
            return render(request, "edit.html", context)
    else:
        form = UpdateUserForm(
            initial={
                "first_name": user.first().first_name,
                "last_name": user.first().last_name,
                "email": user.first().email,
                "telephone": profile.first().phoneNumber,
            }
        )
        context = {
            "form": form,
        }
        return render(request, "edit.html", context)


@csrf_protect
def admin(request):
    # handle GET
    template = loader.get_template("admin.html")
    User = get_user_model()
    users = User.objects.all()
    profiles = Profile.objects.all()
    context = {"users": users, "profiles": profiles}
    return HttpResponse(template.render(context, request))


@csrf_protect
def adminEdit(request, profil_id):
    User = get_user_model()
    user = User.objects.filter(id=profil_id)
    profile = Profile.objects.filter(user_id=profil_id)
    if request.method == "POST":
        body_unicode = request.POST
        user.update(
            username=body_unicode["username"],
            first_name=body_unicode["first_name"],
            last_name=body_unicode["last_name"],
            email=body_unicode["email"],
        )

        profile.update(phoneNumber=body_unicode["phoneNumber"], picture=None)
        usr = User.objects.get(id=request.user.id)
        usr.set_password(body_unicode["password"])
        usr.save()

        return redirect("view-admin")


@csrf_protect
def adminRemove(request, profil_id):
    User = get_user_model()
    user = User.objects.filter(id=profil_id)
    user.delete()

    return redirect("view-admin")
