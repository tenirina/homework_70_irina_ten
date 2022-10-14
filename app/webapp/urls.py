from django.urls import path

from webapp.views.base import IndexView
from webapp.views.issues import IssueView, AddView, UpdateView, DeleteView
from webapp.views.projects import ProjectsView, ProjectUpdateView, ProjectView

urlpatterns = [
    path("", ProjectsView.as_view(), name="projects_list"),
    path("projects/", ProjectsView.as_view(), name="projects_list"),
    path("projects/<int:pk>/update", ProjectUpdateView.as_view(), name="update_project"),
    path("projects/<int:pk>", ProjectView.as_view(), name="project_detail"),
    path("issues/", IndexView.as_view(), name="index"),
    path("issues/<int:pk>", IssueView.as_view(), name="issue_detail"),
    path("issues/add", AddView.as_view(), name="add_issue"),
    path("issues/<int:pk>/update", UpdateView.as_view(), name="update_issue"),
    path("issues/<int:pk>/delete", DeleteView.as_view(), name="delete_issue"),
]
