import random

from django.conf import settings
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_safe

from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, label_suffix='')
        if form.is_valid():
            headers = {'X-Source-IP': request.META['REMOTE_ADDR']}
            EmailMessage('[myks.org] ' + form.cleaned_data['subject'],
                    form.cleaned_data['message'],
                    form.cleaned_data['sender'],
                    settings.CONTACT_EMAILS,
                    headers=headers).send()
            return HttpResponseRedirect(reverse('contact:thanks'))
    else:
        form = ContactForm(initial={'captcha_ref': random.randint(1000, 9999)},
                           label_suffix='')
    context = {'form': form}
    return render(request, 'contact/form.html', context)


@require_safe
def thanks(request, *args):
    return render(request, 'contact/thanks.html')
