from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView

from webapp.forms import IssueForm
from webapp.models import Issue


class IssueView(DetailView):
    template_name = 'issue.html'
    model = Issue


class AddView(CreateView):
    template_name = 'add.html'
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class UpdateView(UpdateView):
    template_name = 'update.html'
    form_class = IssueForm
    model = Issue
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class DeleteView(TemplateView):
    template_name = 'confirm_delete.html'
    model = Issue
    success_url = reverse_lazy('index')
