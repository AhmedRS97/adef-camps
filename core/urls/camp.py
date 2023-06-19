from django.urls import path

from core.views import (
    CampDetailView, CampListView, CampCreateView,
    CampUpdateView, CampDeleteView,
)

urlpatterns = [
    path(
        "camps/", CampListView.as_view(),
        name="camp_list"
    ),
    path(
        "camps/create/", CampCreateView.as_view(),
        name="camp_create"
    ),
    path(
        "camps/<int:pk>/", CampDetailView.as_view(),
        name="camp_detail"
    ),
    path(
        "camps/<int:pk>/update/", CampUpdateView.as_view(),
        name="camp_update"
    ),
    path(
        "camps/<int:pk>/delete/", CampDeleteView.as_view(),
        name="camp_delete"
    ),
]