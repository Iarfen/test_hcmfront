from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_classroom/', views.add_classroom, name='add_classroom'),
    path('add_classroom_send/', views.add_classroom_send, name='add_classroom_send'),
    path('rent_classroom/', views.rent_classroom, name='rent_classroom'),
    path('rent_classroom_send/', views.rent_classroom_send, name='rent_classroom_send'),
    path('request_classroom/', views.request_classroom, name='request_classroom'),
    path('request_classroom_send/', views.request_classroom_send, name='request_classroom_send'),
    path('login/', views.login, name='login'),
    path('search_classroom/', views.search_classroom, name='search_classroom'),
    path('modify_reservation/', views.modify_reservation, name='modify_reservation'),
    path('modify_reservation_edit/', views.modify_reservation_edit, name='modify_reservation_edit'),
    path('modify_reservation_delete/', views.modify_reservation_delete, name='modify_reservation_delete'),
]