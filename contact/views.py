from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ContactForm


class SubmitView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')
    template_name = 'contact/form.html'

    def form_valid(self, form):
        headers = {'X-Source-IP': self.request.META['REMOTE_ADDR']}
        form.send_email(headers)
        return super(SubmitView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'contact/thanks.html'
