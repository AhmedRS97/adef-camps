from django.urls import path

from core.views import (
    TimeSlotDetailView, TimeSlotListView, TimeSlotCreateView,
    TimeSlotUpdateView, TimeSlotDeleteView,
)

urlpatterns = [
    path(
        "timeslots/", TimeSlotListView.as_view(),
        name="timeslot_list"
    ),
    path(
        "timeslots/create/", TimeSlotCreateView.as_view(),
        name="timeslot_create"
    ),
    path(
        "timeslots/<int:pk>/", TimeSlotDetailView.as_view(),
        name="timeslot_detail"
    ),
    path(
        "timeslots/<int:pk>/update/", TimeSlotUpdateView.as_view(),
        name="timeslot_update"
    ),
    path(
        "timeslots/<int:pk>/delete/", TimeSlotDeleteView.as_view(),
        name="timeslot_delete"
    ),
]