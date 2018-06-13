from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.forms import formset_factory
from hcmfront.models import Classroom
from hcmfront.forms import AddClassroomForm,ScheduleForm,InputsForm
import logging


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_classroom(request):
    return render(request, 'add_classroom.html')

def add_classroom_send(request):
#    logger = logging.getLogger(__name__)
#    logger.error('request.POST: '+str(request.POST))
#    logger.error('request.POST: '+str('as'))
#    form = AddClassroomForm(request.POST,len(request.POST['schedule_day[]']))
    form = AddClassroomForm(request.POST)
    ScheduleFormSet = formset_factory(ScheduleForm)
    InputFormSet = formset_factory(InputsForm)
    scheduleformset = ScheduleFormSet(request.POST,prefix='schedule')
    inputformset = InputFormSet(request.POST,prefix='input')
    if (form.is_valid() and scheduleformset.is_valid() and inputformset.is_valid()):
        cs = Classroom(name=request.POST['name'],location=request.POST['location'],capacity=request.POST['capacity'])
        for scheduleform in scheduleformset:
            sc = Classroom_schedule(scheduleform.start_hour,scheduleform.end_hour)
            cs.schedule_set.add(sc)
        for inputform in inputformset:
            ipf = Classroom_input(inputform.name)
            cs.input_set.add(ipf)
        cs.save()
    return render(request, 'add_classroom.html', {'form' : form,'scheduleformset' : scheduleformset,'inputformset' : inputformset})

def login(request):
    return render(request, 'login.html')

def search_classroom(request):
    return render(request, 'search_classroom.html')

def rent_classroom(request):
    return render(request, 'rent_classroom.html')

def rent_classroom_send(request):
    return render(request, 'rent_classroom_send.html')

def request_classroom(request):
    return render(request, 'request_classroom.html')

def request_classroom_send(request):
    return render(request, 'request_classroom_send.html')

def modify_reservation(request):
    return render(request, 'modify_reservation.html')

def modify_reservation_edit(request):
    return render(request, 'modify_reservation_edit.html')

def modify_reservation_delete(request):
    return render(request, 'modify_reservation.html')