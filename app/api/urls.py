from django.urls import path

from api.views import ProjectDetailView, ProjectListView, ProjectUpdateView, ProjectDeleteView, IssueListView, \
    IssueDetailView, IssueUpdateView, IssueDeleteView

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='projects_api'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_api'),
    path('project/update/<int:pk>', ProjectUpdateView.as_view(), name='project_update_api'),
    path('project/delete/<int:pk>', ProjectDeleteView.as_view(), name='project_delete_api'),
    path('issues/', IssueListView.as_view(), name='issues_api'),
    path('issue/<int:pk>', IssueDetailView.as_view(), name='issue_api'),
    path('issue/update/<int:pk>', IssueUpdateView.as_view(), name='issue_update_api'),
    path('issue/delete/<int:pk>', IssueDeleteView.as_view(), name='issue_delete_api'),
]
