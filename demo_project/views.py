from django.shortcuts import render

def index(request):
    return render(request,'demo_project/index.html')


def contact(request):
    return render(request,'demo_project/contact.html')