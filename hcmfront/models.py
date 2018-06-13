from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)


class Classroom_schedule(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    start_hour = models.DateTimeField('date published')
    end_hour = models.DateTimeField('date published')


class Classroom_input(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Reservation(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date = models.DateTimeField('date published')
    start_hour = models.DateTimeField('date published')
    end_hour = models.DateTimeField('date published')
    number_of_people = models.IntegerField(default=0)


class Reservation_input(models.Model):
    classroom_input = models.ForeignKey(Classroom_input, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)