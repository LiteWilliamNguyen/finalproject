from django.urls import path
from . import views

#this is a comment
urlpatterns= [
    path('',views.index, name='index'),
    path('getMedication/', views.getMedication, name="medication"),
    path('getPharmacist/', views.getPharmacist, name="pharmacist"),
    path('getTechnician/', views.getTechnician, name="technician"),
    path('getShift/', views.getShift, name="shift"),
    path('loginmessage/',views.loginMessage, name='loginmessage'),
    path('logoutmessasge/', views.logoutMessage, name="logoutmessage"),
    path('newmedication/', views.newMedication, name="newmedication"),
    path('shiftdetail/<int:id>', views.shiftdetail, name='shiftdetail')
]
