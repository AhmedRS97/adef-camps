from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    DetailView, ListView, CreateView,
    UpdateView, DeleteView
)

from core.forms import TimeSlotForm
from core.models import TimeSlot


class TimeSlotDetailView(PermissionRequiredMixin, DetailView):
    model = TimeSlot
    permission_required = "timeslots.view_timeslot"
    template_name = "core/timeslot/timeslot_detail.html"


class TimeSlotListView(PermissionRequiredMixin, ListView):
    model = TimeSlot
    permission_required = "timeslots.view_timeslot"
    paginate_by = 20
    template_name = "core/timeslot/timeslot_list.html"


class TimeSlotCreateView(PermissionRequiredMixin, CreateView):
    model = TimeSlot
    permission_required = "timeslots.add_timeslot"
    template_name = "core/timeslot/timeslot_form.html"
    form_class = TimeSlotForm


class TimeSlotUpdateView(PermissionRequiredMixin, UpdateView):
    model = TimeSlot
    permission_required = "timeslots.change_timeslot"
    template_name = "core/timeslot/timeslot_form.html"
    form_class = TimeSlotForm


class TimeSlotDeleteView(PermissionRequiredMixin, DeleteView):
    model = TimeSlot
    permission_required = "timeslots.delete_timeslot"
    template_name = "core/timeslot/timeslot_confirm_delete.html"
    success_url = "/"
