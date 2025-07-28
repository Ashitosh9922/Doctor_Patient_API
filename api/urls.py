from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.doctor_list),
    path('doctors/<int:id>/', views.doctor_detail),
    path('doctors/create/', views.create_doctor), 
    path('appointments/', views.book_appointment),
    path('appointments/list/', views.get_appointments),
]
