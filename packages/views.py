from django.shortcuts import render, redirect

from .models import Package, Membership, Payment,Trainer


def package_list(request):

    packages = Package.objects.all()
    trainers = Trainer.objects.all()

    return render(
        request,
        "packages.html",
        {
            "packages": packages,
            "trainers": trainers
        }
    )


def buy_package(request, id):

    package = Package.objects.get(id=id)

    trainer_id = request.POST.get("trainer")

    trainer = None

    if trainer_id:
        trainer = Trainer.objects.get(id=trainer_id)

    total_amount = package.price

    if trainer:
        total_amount += trainer.price

    Membership.objects.create(
        user=request.user,
        package=package,
        trainer=trainer
    )

    Payment.objects.create(
        user=request.user,
        package=package,
        trainer=trainer,
        amount=total_amount
    )

    return redirect("dashboard")
