from django.urls import path

from webapp.views.base import IndexView
from webapp.views.issues import IssueView, AddView, UpdateView, DeleteView
from webapp.views.projects import ProjectsView, ProjectUpdateView, ProjectView, ProjectCreateView, \
    ProjectIssueCreateView, ProjectDeleteView, ProjectsUsersCreateView
from webapp.views.search import SearchView

urlpatterns = [
    path("", ProjectsView.as_view(), name="projects_list"),
    path("projects/", ProjectsView.as_view(), name="projects_list"),
    path("projects/<int:pk>/update", ProjectUpdateView.as_view(), name="update_project"),
    path("projects/<int:pk>", ProjectView.as_view(), name="project_detail"),
    path("projects/create", ProjectCreateView.as_view(), name="project_create"),
    path("projects/<int:pk>/issues/create", ProjectIssueCreateView.as_view(), name="project_issue_create"),
    path("projects/<int:pk>/delete", ProjectDeleteView.as_view(), name="project_delete"),
    path("projects/<int:pk>/user/", ProjectsUsersCreateView.as_view(), name='project_user_create'),
    path("issues/", IndexView.as_view(), name="index"),
    path("issues/<int:pk>", IssueView.as_view(), name="issue_detail"),
    path("issues/create", AddView.as_view(), name="add_issue"),
    path("issues/<int:pk>/update", UpdateView.as_view(), name="update_issue"),
    path("issues/<int:pk>/delete", DeleteView.as_view(), name="delete_issue"),
    path("projects/search", SearchView.as_view(), name='projects_search')
]
