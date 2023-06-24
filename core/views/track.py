from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    DetailView, ListView, CreateView,
    UpdateView, DeleteView
)

from core.forms import TrackForm
from core.models import Track


class TrackDetailView(PermissionRequiredMixin, DetailView):
    model = Track
    permission_required = "tracks.view_track"
    template_name = "core/track/track_detail.html"


class TrackListView(PermissionRequiredMixin, ListView):
    model = Track
    permission_required = "tracks.view_track"
    paginate_by = 20
    template_name = "core/track/track_list.html"


class TrackCreateView(PermissionRequiredMixin, CreateView):
    model = Track
    permission_required = "tracks.add_track"
    template_name = "core/track/track_form.html"
    form_class = TrackForm


class TrackUpdateView(PermissionRequiredMixin, UpdateView):
    model = Track
    permission_required = "tracks.change_track"
    template_name = "core/track/track_form.html"
    form_class = TrackForm


class TrackDeleteView(PermissionRequiredMixin, DeleteView):
    model = Track
    permission_required = "tracks.delete_track"
    template_name = "core/track/track_confirm_delete.html"
    success_url = "/"
