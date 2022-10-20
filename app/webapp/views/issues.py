from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import IssueForm
from webapp.models import Issue


class IssueView(LoginRequiredMixin, DetailView):
    template_name = 'issues/issue.html'
    model = Issue

    def get_object(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        issue = get_object_or_404(Issue, pk=pk)
        if issue.is_deleted:
            raise Http404("Issue deleted")
        return issue


class AddView(LoginRequiredMixin, CreateView):
    template_name = 'issues/add.html'
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class UpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'issues/update.html'
    form_class = IssueForm
    model = Issue
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class DeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'issues/confirm_delete.html'
    model = Issue
    success_url = reverse_lazy('projects_list')

