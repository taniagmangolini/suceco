from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm
from suceco import settings
import logging

logger = logging.getLogger(__name__)

def send_message(request):
    form = ContactForm()
    template_name = 'contact/contact.html'
    context = { 'form' : form }

    try:
        subject = request.POST.get('topic', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        if subject != '' and email != '' and message != '':
            email = EmailMessage(subject, 
                                 message, 
                                 settings.EMAIL_FROM,
                                 [settings.EMAIL_DESTINATION])
            email.send()
            context = {
                'form' : form,
                'msg' : 'The message was sent.',
            }
        return render(request, template_name, context)

    except Exception as e:
        logger.info('[ERROR] sending email {}'.format(str(e)))
        context = {
            'form' : form,
            'msg' : 'It was not possible to send the message.',
        }
        return render(request, template_name, context)