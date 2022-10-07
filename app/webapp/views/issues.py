from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from webapp.forms import IssueForm
from webapp.models import Issue, Status, Type


class IssueView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context


class AddView(TemplateView):
    template_name = 'add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stats = []
        for el in Status.objects.all():
            stats.append((el.pk, el.title))
        context['statuses'] = stats
        types = []
        for el in Type.objects.all():
            types.append((el.pk, el.title))
        context['types'] = types
        return context

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = Issue.objects.create(**form.cleaned_data)
            return redirect('issue_detail', pk=issue.pk)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        issue = {
            'summary': form.data['summary'],
            'description': form.data['description'],
            'status': form.data['status'],
            'type': form.data['type'],
        }
        context['issue'] = issue
        return render(request, 'add.html', context=context)


class UpdateView(TemplateView):
    template_name = 'update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stats = []
        for el in Status.objects.all():
            stats.append((el.pk, el.title))
        context['statuses'] = stats
        types = []
        for el in Type.objects.all():
            types.append((el.pk, el.title))
        context['types'] = types
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(instance=issue)
        print(context['issue'].status.pk)
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_detail', pk=kwargs['pk'])
        context = self.get_context_data(**kwargs)
        context['form'] = form
        issue = {
            'pk': kwargs['pk'],
            'summary': form.data['summary'],
            'description': form.data['description'],
            'status': form.data['status'],
            'type': form.data['type'],
        }
        context['issue'] = issue
        return render(request, 'add.html', context=context)


class DeleteView(TemplateView):
    template_name = 'update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stats = []
        for el in Status.objects.all():
            stats.append((el.pk, el.title))
        context['statuses'] = stats
        types = []
        for el in Type.objects.all():
            types.append((el.pk, el.title))
        context['types'] = types
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_detail', pk=kwargs['pk'])
        context = self.get_context_data(**kwargs)
        context['form'] = form
        issue = {
            'pk': kwargs['pk'],
            'summary': form.data['summary'],
            'description': form.data['description'],
            'status': form.data['status'],
            'type': form.data['type'],
        }
        context['issue'] = issue
        return render(request, 'add.html', context=context)
