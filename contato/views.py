from .forms import ContatoForm
from django.shortcuts import render, redirect
from suceco import settings
from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
import logging

logger = logging.getLogger(__name__)


def mandar_mensagem_old(request):
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
            logger.info('EMAIL_PORT ' +  str(settings.EMAIL_PORT))
            logger.info('EMAIL_HOST_PASSWORD ' +  settings.EMAIL_HOST_PASSWORD)

            message = Mail(
                from_email=settings.EMAIL_HOST_USER,
                to_emails=settings.EMAIL_HOST_USER,
                subject='SUCECO',
                html_content= mensagem + '. Email contato: ' + email_contato)

            try:
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(message)
                logger.info('msg sent ')
                contexto = {
                    'form' : form,
                    'msg' : 'Mensagem enviada',
                }

            except Exception as e:
                logger.info('[ERRO] sending email')
                logger.error(e)
                contexto = {
                    'form' : form,
                    'msg' : 'Não foi possível enviar a enviar mensagem.',
                }

        return render(request, template_name, contexto)