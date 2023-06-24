from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    DetailView, ListView, CreateView,
    UpdateView, DeleteView
)

from core.forms import CampForm
from core.models import Camp


class CampDetailView(PermissionRequiredMixin, DetailView):
    model = Camp
    permission_required = "camps.view_camp"
    template_name = "core/camp/camp_detail.html"


class CampListView(PermissionRequiredMixin, ListView):
    model = Camp
    permission_required = "camps.view_camp"
    paginate_by = 20
    template_name = "core/camp/camp_list.html"


class CampCreateView(PermissionRequiredMixin, CreateView):
    model = Camp
    permission_required = "camps.add_camp"
    template_name = "core/camp/camp_form.html"
    form_class = CampForm


class CampUpdateView(PermissionRequiredMixin, UpdateView):
    model = Camp
    permission_required = "camps.change_camp"
    template_name = "core/camp/camp_form.html"
    form_class = CampForm


class CampDeleteView(PermissionRequiredMixin, DeleteView):
    model = Camp
    permission_required = "camps.delete_camp"
    template_name = "core/camp/camp_confirm_delete.html"
    success_url = "/"
