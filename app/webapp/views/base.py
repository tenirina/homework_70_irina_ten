
from django.views.generic import TemplateView

from webapp.models import Issue, Status


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.filter(is_deleted=False)
        return context



