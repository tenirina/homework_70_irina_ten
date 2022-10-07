
from django.views.generic import TemplateView

from webapp.models import Issue, Status


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        statuses = Status.objects.all()
        issues = Issue.objects.all()
        # for el in issues:
        #     for status in statuses:
        #         if status == el.status:
        #             el.status = Status.objects.get(status)
        context['issues'] = issues
        return context



