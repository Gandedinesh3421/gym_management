from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Profile
from packages.models import Membership, Payment


def register(request):

    if request.method == "POST":

        user = User.objects.create_user(

            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password']

        )

        Profile.objects.create(
            user=user,
            phone=request.POST['phone']
        )

        return redirect("login")

    return render(request, "register.html")


def user_login(request):

    if request.method == "POST":

        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user:

            login(request, user)

            return redirect("dashboard")

    return render(request, "login.html")


def dashboard(request):

    membership = Membership.objects.filter(
        user=request.user
    ).last()

    payments = Payment.objects.filter(
        user=request.user
    )

    return render(
        request,
        "dashboard.html",
        {
            "membership": membership,
            "payments": payments
        }
    )


from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    return render(request, 'profile.html', {
        'profile': profile
    })


def payment_history(request):

    payments = Payment.objects.filter(
        user=request.user
    )

    return render(
        request,
        "payment_history.html",
        {"payments": payments}
    )


def user_logout(request):

    logout(request)

    return redirect("login")