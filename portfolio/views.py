from django.shortcuts import render
from .forms import ContactForm


def index(request):
    return render(request, "portfolio/index.html")

def about(request):
    return render(request, "portfolio/about.html")

def contact(request):
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, "portfolio/contact.html", context)

def work(request):
    return render(request, "portfolio/work.html")
