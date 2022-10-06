from django.shortcuts import render


def index_view(require):
    return render(require, "index")
