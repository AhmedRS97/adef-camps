from django.db import models


class Session(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    capacity = models.IntegerField()
    link = models.URLField()
    trainer = models.ForeignKey(
        "Trainer", related_name="sessions",
        blank=True, null=True, on_delete=models.SET_NULL
    )
    track = models.ForeignKey(
        "Track", related_name="sessions",
        blank=True, null=True, on_delete=models.SET_NULL
    )


class Track(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
