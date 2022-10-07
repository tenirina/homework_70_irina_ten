from django.urls import path

from webapp.views.base import IndexView
from webapp.views.issues import IssueView, AddView, UpdateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("issues/", IndexView.as_view(), name="index"),
    path("issues/<int:pk>", IssueView.as_view(), name="issue_detail"),
    path("issues/add", AddView.as_view(), name="add_issue"),
    path("issues/<int:pk>", UpdateView.as_view(), name="update_issue")
]