from django.http import HttpResponse


def show_map(request):
    return HttpResponse('<h1>Здесь будет карта</h1>')