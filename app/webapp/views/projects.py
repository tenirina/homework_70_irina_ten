from django.urls import reverse
from django.views.generic import ListView, UpdateView, DetailView

from webapp.forms import ProjectForm
from webapp.models import Project


class ProjectsView(ListView):
    template_name = "projects/projects_list.html"
    model = Project
    context_object_name = 'projects'
    paginate_by = 3
    paginate_orphans = 1


class ProjectUpdateView(UpdateView):
    template_name = "projects/project_update.html"
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectView(DetailView):
    template_name = "projects/project.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        issues = project.issue.filter(is_deleted=False)
        print(issues)
        context['issues'] = issues
        return context

