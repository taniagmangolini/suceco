from django.shortcuts import render


def index(request):
    '''
    :param request:
    :return: main page
    '''
    return render(request, 'registros/list.html', {})
