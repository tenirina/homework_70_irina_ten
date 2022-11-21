from django.urls import path

from api.views import ProjectDetailView, ProjectListView, ProjectUpdateView, ProjectDeleteView,

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='projects_api'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_api'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update_api'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete_api'),

