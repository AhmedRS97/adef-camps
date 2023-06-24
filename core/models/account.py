from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars")


class Manager(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()


class Trainer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
    title = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.user.get_full_name()


class Trainee(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
    age = models.DateTimeField()
    bio = models.TextField()
    group = models.ForeignKey(
        "TraineeGroup", related_name="trainees",
        on_delete=models.CASCADE
    )
    track = models.ForeignKey(
        "Track", related_name="trainees",
        blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.user.get_full_name()


class TraineeGroup(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("traineegroup_detail", kwargs={"pk": self.pk})
