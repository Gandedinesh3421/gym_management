from django.db import models
from django.contrib.auth.models import User
from datetime import date, timedelta


class Package(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return self.name


# ✅ NEW MODEL
class Trainer(models.Model):

    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200)
    experience = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Membership(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    # ✅ add trainer
    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    start_date = models.DateField(auto_now_add=True)
    payment_status = models.BooleanField(default=True)

    def expiry_date(self):
        return self.start_date + timedelta(days=self.package.duration)

    def days_left(self):
        return (self.expiry_date() - date.today()).days


class Payment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    trainer = models.ForeignKey(
        Trainer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    amount = models.IntegerField()
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="Paid")
