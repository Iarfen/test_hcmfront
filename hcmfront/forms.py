from django import forms
import logging

class AddClassroomForm(forms.Form):
    name = forms.CharField(max_length=255)
    location = forms.CharField(max_length=255)
    capacity = forms.IntegerField()

#    def __init__(self,post,schedules_number):
#        super(AddClassroomForm,self).__init__(post)
#        schedule_day = []
#        schedule_start_date = []
#        schedule_end_date = []
#        for x in range(0,schedules_number):
#            logger = logging.getLogger(__name__)
#            logger.error('x value: '+str(x))
#            schedule_day.append(forms.IntegerField())
#            schedule_start_date.append(forms.IntegerField())
#            schedule_end_date.append(forms.IntegerField())

class ScheduleForm(forms.Form):
    day = forms.IntegerField()
    start_hour = forms.TimeField()
    end_hour = forms.TimeField()

class InputsForm(forms.Form):
    name = forms.CharField()