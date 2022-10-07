from django.urls import path

from webapp.views.base import IndexView
from webapp.views.issues import IssueView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("issues/", IndexView.as_view(), name="index"),
    path("issues/<int:pk>", IssueView.as_view(), name="issue_detail")
]