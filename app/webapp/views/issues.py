from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import IssueForm
from webapp.models import Issue


class IssueView(DetailView):
    template_name = 'issues/issue.html'
    model = Issue


class AddView(CreateView):
    template_name = 'issues/add.html'
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class UpdateView(UpdateView):
    template_name = 'issues/update.html'
    form_class = IssueForm
    model = Issue
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class DeleteView(DeleteView):
    template_name = 'issues/confirm_delete.html'
    model = Issue
    success_url = reverse_lazy('projects_list')

