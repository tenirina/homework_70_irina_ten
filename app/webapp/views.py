from django.shortcuts import render

from webapp.forms import IssueForm


def index_view(require):
    form = IssueForm()
    return render(require, "index.html", context={'form': form})
