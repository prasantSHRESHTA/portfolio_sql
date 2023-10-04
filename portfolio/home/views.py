from django.shortcuts import render
from django.core.mail import send_mail
from home import models
from home.models import projects, resume, edu, exp
from django.conf import settings


def home(request):
    return render(request, 'home.html')


def work(request):
    proj = projects.objects.all()

    return render(request, 'work.html', {'proj': proj})


def education(request):
    educ = edu.objects.all()

    return render(request, 'education.html', {'educ': educ})


def Resume(request):
    res = resume.objects.all()
    return render(request, 'resume.html', {'res': res})


def contact(request):
    if request.method == "POST":
        Firstname = request.POST.get("FirstName")
        Lastname = request.POST.get("LastName")
        email = request.POST.get("Email")
        phone = request.POST.get("PhoneNumber")
        mail = request.POST.get("content")

        from_email = settings.EMAIL_HOST_USER

        send_mail("Contact", mail + "(" + phone + ")" + " ( " + email + " ) ", from_email,
                  ["prasantpradhankuma4@gmail.com"])

    return render(request, 'contact.html')


def experience(request):
    experience = exp.objects.all()

    return render(request, 'exp.html', {"experience": experience})
