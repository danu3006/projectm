from django.views.generic import TemplateView

from .models import Category


class IndexView(TemplateView):
    template_name = 'itemsdb/includes/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'categories': Category.objects.all(),
        })

        return context
