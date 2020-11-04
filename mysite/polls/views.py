from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    return render(request, 'polls/index.html')


def about(request):
    return render(request, 'polls/about.html')


def contact(request):
    if request.method == 'POST':
        try:
            email = request.POST['Email']
            subject = request.POST['Subject']
            message = request.POST['Message']
            models.mywebsitedb(email=email, subject=subject, message=message).save()
            return render(request, 'polls/ThankYou.html')
        except:
            return render(request, 'polls/contact.html')
    return render(request, 'polls/contact.html')

def works(request):
    return render(request, 'polls/works.html')


def pythondevloper(request):
    return render(request, 'polls/pythondevloper.html')


def frontendwebdevlopment(request):
    return render(request, 'polls/frontendwebdevlopment.html')


def backend(request):
    return render(request, 'polls/backenddevloper.html')








