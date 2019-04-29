from django.http import HttpResponse


def hello(request):
    return HttpResponse("Let's try add  '/api/' or '/api/images/' to your url")
