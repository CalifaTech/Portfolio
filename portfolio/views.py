from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Welcome to my portfolio!")

def resume(request):
    return HttpResponse("This is my resume page.")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def work(request):
    return HttpResponse("This is the projects page.")