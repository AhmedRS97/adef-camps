from django.db import models


class Space(models.Model):
    name = models.CharField(max_length=100)


class TimeSlot(models.Model):
    name = models.CharField(max_length=50)


class Allocation(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    capacity = models.IntegerField()
    time_slot = models.ForeignKey(
        TimeSlot, related_name="allocations", on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        "TraineeGroup", related_name="allocations",
        blank=True, null=True, on_delete=models.SET_NULL
    )
    space = models.ForeignKey(
        "Space", related_name="allocations",
        blank=True, null=True, on_delete=models.SET_NULL
    )
    trainees = models.ManyToManyField(
        "Trainee", related_name="allocations"
    )
    sessions = models.ManyToManyField(
        "Session", related_name="allocations"
    )


class Camp(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
