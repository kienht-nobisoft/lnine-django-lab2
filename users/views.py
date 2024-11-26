from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.utils.translation import activate
from django.shortcuts import render, redirect
from users.models import UserProfile


def index(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect("login-view")

    context = {"full_name": f"{user.first_name} {user.last_name}"}
    user_profile = UserProfile.objects.filter(user=user).first()
    activate(user_profile.language_code)

    return render(request, "users/index.html", context)


def login_view(request):
    return render(request, "users/pages-login.html")


def login_user(request):
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        raise Http404("User not found")


def logout_user(request):
    logout(request)
    return redirect("login-view")


def change_password_view(request):
    return render(request, "users/pages-changepw-new.html")


def change_password(request):
    if not request.user.is_authenticated:
        return redirect("login-view")

    user = request.user

    old_password = request.POST["old_password"]
    new_password = request.POST["new_password"]
    confirm_password = request.POST["confirm_password"]

    if new_password != confirm_password:
        raise Http404("Wrong confirm password")
    if user.check_password(old_password) is False:
        raise Http404("Wrong old password")

    user.set_password(confirm_password)
    user.save()
    logout(request)
    return redirect("login-view")


def recover_password_view(request):
    return render(request, "users/pages-recoverpw.html")


def change_language(request):
    if not request.user.is_authenticated:
        return redirect("login-view")

    user = request.user
    user_profile = UserProfile.objects.filter(user=user).first()
    user_profile.language_code = request.GET["lang"]
    user_profile.save(update_fields=["language_code"])

    return redirect("index")
