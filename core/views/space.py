from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    DetailView, ListView, CreateView,
    UpdateView, DeleteView
)

from core.forms import SpaceForm
from core.models import Space


class SpaceDetailView(PermissionRequiredMixin, DetailView):
    model = Space
    permission_required = "spaces.view_space"
    template_name = "core/space/space_detail.html"


class SpaceListView(PermissionRequiredMixin, ListView):
    model = Space
    permission_required = "spaces.view_space"
    paginate_by = 20
    template_name = "core/space/space_list.html"


class SpaceCreateView(PermissionRequiredMixin, CreateView):
    model = Space
    permission_required = "spaces.add_space"
    template_name = "core/space/space_form.html"
    form_class = SpaceForm


class SpaceUpdateView(PermissionRequiredMixin, UpdateView):
    model = Space
    permission_required = "spaces.change_space"
    template_name = "core/space/space_form.html"
    form_class = SpaceForm


class SpaceDeleteView(PermissionRequiredMixin, DeleteView):
    model = Space
    permission_required = "spaces.delete_space"
    template_name = "core/space/space_confirm_delete.html"
    success_url = "/"
