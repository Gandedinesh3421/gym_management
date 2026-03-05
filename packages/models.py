from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    duration=models.IntegerField()

class Membership(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    package=models.ForeignKey(Package,on_delete=models.CASCADE)
    payment_status=models.BooleanField(default=True)
