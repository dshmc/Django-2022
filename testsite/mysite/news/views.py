from django.http import HttpResponse
# Create your views here.
def index(request):
    print(request)
    return HttpResponse('<h1>Hello world</h1>')

def test(request):
    return HttpResponse('<h1> Тестова сторінка </h1>')