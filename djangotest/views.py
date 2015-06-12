from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def toomanyargssum(x1, x2, x3, x4, x5, x6, x7, x8, x9):
    x = x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9
    return x