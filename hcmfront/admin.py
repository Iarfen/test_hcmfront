from django.contrib import admin

from .models import Classroom,Classroom_schedule,Classroom_input,Reservation,Reservation_input

admin.site.register(Classroom)
admin.site.register(Classroom_schedule)
admin.site.register(Classroom_input)
admin.site.register(Reservation)
admin.site.register(Reservation_input)