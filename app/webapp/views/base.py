
from django.views.generic import ListView

from webapp.models import Issue


class IndexView(ListView):
    template_name = 'issues/index.html'
    model = Issue
    context_object_name = 'issues'
    paginate_by = 3
    paginate_orphans = 1
    queryset = Issue.objects.exclude(is_deleted=True)
