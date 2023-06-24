from django.urls import path

from core.views import (
    SpaceDetailView, SpaceListView, SpaceCreateView,
    SpaceUpdateView, SpaceDeleteView,
)

urlpatterns = [
    path(
        "spaces/", SpaceListView.as_view(),
        name="space_list"
    ),
    path(
        "spaces/create/", SpaceCreateView.as_view(),
        name="space_create"
    ),
    path(
        "spaces/<int:pk>/", SpaceDetailView.as_view(),
        name="space_detail"
    ),
    path(
        "spaces/<int:pk>/update/", SpaceUpdateView.as_view(),
        name="space_update"
    ),
    path(
        "spaces/<int:pk>/delete/", SpaceDeleteView.as_view(),
        name="space_delete"
    ),
]