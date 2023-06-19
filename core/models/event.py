from django.db import models


class Space(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("space_detail", kwargs={"pk": self.pk})


class TimeSlot(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("timeslot_detail", kwargs={"pk": self.pk})


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

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("allocation_detail", kwargs={"pk": self.pk})


class Camp(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"معسكر {self.start_date.year} - {self.end_date.year}"

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("camp_detail", kwargs={"pk": self.pk})
