from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm
from suceco import settings
import logging

logger = logging.getLogger(__name__)

def send_message(request):
    form = ContactForm(request.POST)
    template_name = 'contact/contact.html'
    context = { 'form' : form }

    try:
        if form.is_valid():
            subject = request.POST.get('topic', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            email = EmailMessage(subject, 
                                 message + '. From: {}'.format(email),
                                 settings.EMAIL_FROM,
                                 [settings.EMAIL_DESTINATION])
            email.send()
            context = {
                'form' : form,
                'msg' : 'Mensagem enviada.',
            }
        return render(request, template_name, context)

    except Exception as e:
        logger.info('[ERROR] sending email {}'.format(str(e)))
        context = {
            'form' : form,
            'msg' : 'Erro ao enviar mensagem.',
        }
        return render(request, template_name, context)