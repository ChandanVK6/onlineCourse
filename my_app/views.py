from django.shortcuts import render,redirect
from .models import Courses
from .models import User
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages


def index(request):
    return render(request,'base.html')

def login(request):
    if request.method=="POST":
        
        email = request.POST['Email']
        passw = request.POST['password']
        for usr in User.objects.all():
            if email ==usr.email and passw ==usr.passwd:
                return render(request,'user_page.html',{'usr':usr})

    return render(request,'login.html')

def signup(request):

    if request.method=="POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['Email']
        passw = request.POST['password']
        sex = request.POST['sex']

        u = User(fname=fname,lname=lname,email=email,passwd=passw,sex=sex)
        for usr in User.objects.all():
            if fname == usr.fname and lname == usr.lname:
                return HttpResponse(request,'exit')
        u.save()
        
        for usr in User.objects.all():
            if fname == usr.fname and lname == usr.lname:
                return render (request,'user_page.html',{'usr':usr})
    return render(request,'signup.html')

def instructor(request):
    return render(request,'instructor.html')

def instsignup(request):
    return render(request,'inst_signup.html')

def instlogin(request):
    return render(request ,'inst_login.html')

def userpage(request):
    return render(request,'user_page.html')

def mycourse(request):
    my_courses = Courses.objects.all()
    return render(request,'mycourse.html',{'usr':my_courses})