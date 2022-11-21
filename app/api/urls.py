from django.urls import path

from api.views import ProjectDetailView, ProjectListView, ProjectUpdateView, ProjectDeleteView, IssueListView, \
    IssueDetailView, IssueUpdateView, IssueDeleteView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='projects_api'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_api'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update_api'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete_api'),
    path('issues/', IssueListView.as_view(), name='issues_api'),
    path('issue/<int:pk>', IssueDetailView.as_view(), name='issue_api'),
    path('issue/<int:pk>/update', IssueUpdateView.as_view(), name='issue_update_api'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='issue_delete_api'),
]
