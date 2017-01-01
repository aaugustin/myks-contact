from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase


class ContactTests(TestCase):

    def test_contact(self):
        response = self.client.get(reverse('contact:form'))
        self.assertTemplateUsed(response, 'contact/form.html')

    def test_contact_success(self):
        response = self.client.post(reverse('contact:form'), {
            'captcha': "1234",
            'captcha_ref': "1234",
            'sender': "seo@hacker.com",
            'subject': "I can't read!",
            'message': "And I like spamming.",
        })
        self.assertRedirects(response, reverse('contact:thanks'))
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(["charlie@example.com"], mail.outbox[0].to)
        self.assertEqual(["seo@hacker.com"], mail.outbox[0].reply_to)
        self.assertIn("I can't read!", mail.outbox[0].subject)
        self.assertIn("And I like spamming.", mail.outbox[0].body)

    def test_contact_failed_captcha(self):
        response = self.client.post(reverse('contact:form'), {
            'captcha': "1234",
            'captcha_ref': "4321",
            'sender': "seo@hacker.com",
            'subject': "I can't read!",
            'message': "And I like spamming.",
        })
        self.assertFormError(response, 'form', 'captcha',
            "This code isn't valid.")
