from django.urls import path

from core.views import (
    TrackDetailView, TrackListView, TrackCreateView,
    TrackUpdateView, TrackDeleteView,
)

urlpatterns = [
    path(
        "tracks/", TrackListView.as_view(),
        name="track_list"
    ),
    path(
        "tracks/create/", TrackCreateView.as_view(),
        name="track_create"
    ),
    path(
        "tracks/<int:pk>/", TrackDetailView.as_view(),
        name="track_detail"
    ),
    path(
        "tracks/<int:pk>/update/", TrackUpdateView.as_view(),
        name="track_update"
    ),
    path(
        "tracks/<int:pk>/delete/", TrackDeleteView.as_view(),
        name="track_delete"
    ),
]
