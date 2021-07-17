from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from .tokens import confirm_email_token_generator


def send_confirmation_email(request, user):
    token = confirm_email_token_generator.make_token(user)
    uid = user.pk
    domain = get_current_site(request)

    subject = 'activate your account'

    message = render_to_string('registration/account-activation-email.html', 
                                {
                                    'user': user,
                                    'domain': domain,
                                    'uid': uid,
                                    'token': token
                                })

    user.email_user(subject, message)