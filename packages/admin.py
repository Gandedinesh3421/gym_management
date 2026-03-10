from django.contrib import admin
from .models import Package, Membership,Trainer

admin.site.register(Package)

admin.site.register(Membership)
admin.site.register(Trainer)