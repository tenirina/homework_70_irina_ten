from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView

from webapp.forms import UserForm
from webapp.models import Project


class ProjectsUsersCreateView(TemplateView):
    template_name = 'users/users_create.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = Project.objects.filter(pk=kwargs['pk'])[0]
        context['project'] = project
        context['form'] = UserForm
        context['users'] = User.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['users']
            if User.objects.filter(username=user):
                project = Project.objects.filter(pk=kwargs['pk'])[0]
                project.users.add(User.objects.filter(username=user))
            return redirect('projects_list')
        return redirect('projects_list')



