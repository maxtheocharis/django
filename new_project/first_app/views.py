from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def ekpa(request):
    return render(request, 'ekpa.html')
# def home(request):
#     return HttpResponse("Hello, world. You're at the polls index.")