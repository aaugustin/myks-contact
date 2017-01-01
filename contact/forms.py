import random

from django.conf import settings
from django.core.mail import EmailMessage
from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    captcha_ref = forms.IntegerField(widget=forms.HiddenInput)
    captcha = forms.IntegerField(label=_("Code"), help_text=_("This is a shield against bots, a basic <a href=\"http://en.wikipedia.org/wiki/Captcha\">CAPTCHA</a>."))
    sender = forms.EmailField(label=_("Your e-mail"), help_text=_("Give me a valid e-mail address, otherwise I won't be able to answer."))
    subject = forms.CharField(label=_("Subject"))
    message = forms.CharField(label=_("Message"), widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        if not self.is_bound:
            self.initial['captcha_ref'] = random.randint(1000, 9999)

    def clean_captcha(self):
        value = self.cleaned_data['captcha']
        if value != self.cleaned_data.get('captcha_ref'):
            raise forms.ValidationError(_("This code isn't valid."))
        return value

    def send_email(self, headers):
        EmailMessage(
            subject=settings.EMAIL_SUBJECT_PREFIX + self.cleaned_data['subject'],
            body=self.cleaned_data['message'],
            to=settings.CONTACT_EMAILS,
            reply_to=[self.cleaned_data['sender']],
            headers=headers,
        ).send()
