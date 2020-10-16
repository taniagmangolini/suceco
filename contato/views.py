from django.shortcuts import render
from .forms import ContatoForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from suceco import settings

def mandar_mensagem(request):
    form = ContatoForm()
    template_name = 'contato/contato.html'
    contexto = {  }

    try:
        assunto = request.POST.get('assunto', '')
        email_contato  =  request.POST.get('email', '')
        mensagem = request.POST.get('mensagem', '')

        if assunto != '' and email_contato != '' and mensagem != '':

            send_mail(
                assunto,
                mensagem + '. Email contato: ' + email_contato,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            contexto = {
                'msg' : 'Mensagem enviada',
            }

        return render(request, template_name, contexto)

    except:
        contexto = {
            'msg' : 'Erro ao enviar mensagem',
        }
        return render(request, template_name, contexto)