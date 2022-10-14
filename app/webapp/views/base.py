from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import ListView


from webapp.forms import SearchForm
from webapp.models import Issue, Status


class IndexView(ListView):
    template_name = 'issues/index.html'
    model = Issue
    context_object_name = 'issues'
    paginate_by = 3
    paginate_orphans = 1
    queryset = Issue.objects.exclude(is_deleted=True)

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search_value')
        return None

    def get_queryset(self):
        queryset = super().get_queryset().exclude(is_deleted=True)
        print(self.search_value)
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
            print(self.search_value)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context







