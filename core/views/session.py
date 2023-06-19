from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import (
    DetailView, ListView, CreateView,
    UpdateView, DeleteView
)

from core.forms import SessionForm
from core.models import Session


class SessionDetailView(PermissionRequiredMixin, DetailView):
    model = Session
    permission_required = "sessions.view_session"
    template_name = "core/session/session_detail.html"


class SessionListView(PermissionRequiredMixin, ListView):
    model = Session
    permission_required = "sessions.view_session"
    paginate_by = 20
    template_name = "core/session/session_list.html"


class SessionCreateView(PermissionRequiredMixin, CreateView):
    model = Session
    permission_required = "sessions.add_session"
    template_name = "core/session/session_form.html"
    form_class = SessionForm


class SessionUpdateView(PermissionRequiredMixin, UpdateView):
    model = Session
    permission_required = "sessions.change_session"
    template_name = "core/session/session_form.html"
    form_class = SessionForm


class SessionDeleteView(PermissionRequiredMixin, DeleteView):
    model = Session
    permission_required = "sessions.delete_session"
    template_name = "core/session/session_confirm_delete.html"
    success_url = "/"
