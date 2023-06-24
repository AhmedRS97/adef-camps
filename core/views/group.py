from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    DetailView, ListView, CreateView,
    UpdateView, DeleteView
)

from core.forms import TraineeGroupForm
from core.models import TraineeGroup


class TraineeGroupDetailView(PermissionRequiredMixin, DetailView):
    model = TraineeGroup
    permission_required = "traineegroups.view_traineegroup"
    template_name = "core/traineegroup/traineegroup_detail.html"


class TraineeGroupListView(PermissionRequiredMixin, ListView):
    model = TraineeGroup
    permission_required = "traineegroups.view_traineegroup"
    paginate_by = 20
    template_name = "core/traineegroup/traineegroup_list.html"


class TraineeGroupCreateView(PermissionRequiredMixin, CreateView):
    model = TraineeGroup
    permission_required = "traineegroups.add_traineegroup"
    template_name = "core/traineegroup/traineegroup_form.html"
    form_class = TraineeGroupForm


class TraineeGroupUpdateView(PermissionRequiredMixin, UpdateView):
    model = TraineeGroup
    permission_required = "traineegroups.change_traineegroup"
    template_name = "core/traineegroup/traineegroup_form.html"
    form_class = TraineeGroupForm


class TraineeGroupDeleteView(PermissionRequiredMixin, DeleteView):
    model = TraineeGroup
    permission_required = "traineegroups.delete_traineegroup"
    template_name = "core/traineegroup/traineegroup_confirm_delete.html"
    success_url = "/"
