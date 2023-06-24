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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("session_detail", kwargs={"pk": self.pk})


class Track(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("track_detail", kwargs={"pk": self.pk})
