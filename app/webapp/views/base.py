
from django.views.generic import ListView

from webapp.models import Issue, Status


class IndexView(ListView):
    template_name = 'index.html'
    model = Issue
    context_object_name = 'issues'
    paginate_by = 2
    paginate_orphans = 1





