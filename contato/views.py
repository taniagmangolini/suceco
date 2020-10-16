from django.shortcuts import render
from .forms import ContatoForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from suceco import settings
import logging

logger = logging.getLogger(__name__)

def mandar_mensagem(request):
    form = ContatoForm()
    template_name = 'contato/contato.html'
    contexto = {'form' : form  }

    try:
        assunto = request.POST.get('assunto', '')
        email_contato  =  request.POST.get('email', '')
        mensagem = request.POST.get('mensagem', '')

        if assunto != '' and email_contato != '' and mensagem != '':
            logger.info('sending msg ' )
            logger.info('message ' + mensagem )
            logger.info('assunto ' + assunto )
            logger.info('email ' + email_contato )

            logger.info('EMAIL_HOST_USER ' +  settings.EMAIL_HOST_USER)
            logger.info('EMAIL_HOST ' +  settings.EMAIL_HOST)
            logger.info('EMAIL_PORT ' +  settings.EMAIL_PORT)
            logger.info('EMAIL_HOST_PASSWORD ' +  settings.EMAIL_HOST_PASSWORD)
            logger.info('EMAIL_HOST_PASSWORD ' +  settings.EMAIL_HOST_PASSWORD)

            send_mail(
                assunto,
                (mensagem + '. Email contato: ' + email_contato),
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            logger.info('msg sent ')
            contexto = {
                'form' : form,
                'msg' : 'Mensagem enviada',
            }

        return render(request, template_name, contexto)

    except:
        logger.info('error sending msg')
        contexto = {
            'form' : form,
            'msg' : 'Erro ao enviar mensagem',
        }
        return render(request, template_name, contexto)