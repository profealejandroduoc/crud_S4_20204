from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'crud/index.html')


def personas(request):
    return render(request,'crud/personas.html')