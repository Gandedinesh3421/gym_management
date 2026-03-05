from django.urls import path
from . import views

urlpatterns=[
path('',views.package_list,name='packages'),
path('buy/<int:id>/',views.buy_package,name='buy'),
]
