from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from suceco import settings
import logging

logger = logging.getLogger(__name__)

def send_message(request):
    form = ContactForm()
    template_name = 'contact/contact.html'
    contexto = {'form' : form  }

    try:
        topic = request.POST.get('topic', '')
        email  =  request.POST.get('email', '')
        message = request.POST.get('message', '')

        if topic != '' and email != '' and message != '':
            logger.info('sending msg ' )
            logger.info('message ' + message )
            logger.info('topic ' + topic )
            logger.info('email ' + email )

            logger.info('EMAIL_HOST_USER ' +  settings.EMAIL_HOST_USER)
            logger.info('EMAIL_HOST ' +  settings.EMAIL_HOST)
            logger.info('EMAIL_PORT ' +  str(settings.EMAIL_PORT))
            logger.info('EMAIL_HOST_PASSWORD ' +  settings.EMAIL_HOST_PASSWORD)

            send_mail(
                topic,
                (message + '. Email: ' + email),
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_DESTINATARIO],
                fail_silently=False,
            )

            logger.info('msg sent ')
            contexto = {
                'form' : form,
                'msg' : 'The message was sent.',
            }

        return render(request, template_name, contexto)

    except Exception as e:
        logger.info('[ERROR] sending email')
        logger.error(e)
        context = {
            'form' : form,
            'msg' : 'It was not possible to send the message.',
        }
        return render(request, template_name, context)