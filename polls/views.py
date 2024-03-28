from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def jy(request):
    return HttpResponse("어서오세요")

def cafe(request):
    return HttpResponse("아메리카노")