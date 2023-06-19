from django.urls import path

from core.views import (
    TraineeGroupDetailView, TraineeGroupListView, TraineeGroupCreateView,
    TraineeGroupUpdateView, TraineeGroupDeleteView,
)

urlpatterns = [
    path(
        "traineegroups/", TraineeGroupListView.as_view(),
        name="traineegroup_list"
    ),
    path(
        "traineegroups/create/", TraineeGroupCreateView.as_view(),
        name="traineegroup_create"
    ),
    path(
        "traineegroups/<int:pk>/", TraineeGroupDetailView.as_view(),
        name="traineegroup_detail"
    ),
    path(
        "traineegroups/<int:pk>/update/", TraineeGroupUpdateView.as_view(),
        name="traineegroup_update"
    ),
    path(
        "traineegroups/<int:pk>/delete/", TraineeGroupDeleteView.as_view(),
        name="traineegroup_delete"
    ),
]