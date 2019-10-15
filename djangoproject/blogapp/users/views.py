from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import Adduser
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from random import randint
# Create your views here.

def index(request):
    return render(request,'users/header.html')
    #return HttpResponse("<h1>Welcome to users app</h1>")

def login(request):
    if request.session.get('email'):
        return render(request,"users/afterlogin.html")
    else:
        f= Login()
        return render(request,"users/login.html",{'form':f})

def signup(request):
    f = Signup()
    return render(request,"users/signup.html",{'form':f})

def login1(request):
    f = Login(request.POST)
    if f.is_valid():
        email = f.cleaned_data['email']
        password = f.cleaned_data['password']
        try:
            u = Adduser.objects.get(email=email)
        except Adduser.DoesNotExist as e:
            error = "No such user"
            form = Login()
            return render(request,"users/login.html",{'error':error,'form':form})
        else:
            if u.password == password:
                request.session['email'] = email
                return render(request,"users/afterlogin.html")
                #return HttpResponse("Email : {} and password : {}".format(email,password))
            else:
                error = "Password does not matched"
                form = Login()
                return render(request,"users/login.html",{'error':error,'form':form})
        
    else:
        error = "Invalid form"
        f = Login()
        return render(request,"login.html",{'error':error,'form':f})

class Signup1(View):
    def get(self,request):
        error = "No get request handled"
        form = Signup()
        return render(request,"users/signup.html",{'form':form,'error':error})
    
    def post(self,request):
        form = Signup(request.POST,request.FILES)
        if form.is_valid():
            pswd = form.cleaned_data['password']
            cpswd = form.cleaned_data['confirm_password']
            if pswd == cpswd:
                data = {
                    'firstname' : form.cleaned_data['first_name'],
                    'lastname' : form.cleaned_data['last_name'],
                    'email' : form.cleaned_data['email'],
                    'password' : pswd,
                    'pic' : form.cleaned_data['pic'],
                    }
                new_obj = Adduser.objects.create(**data)
                new_obj.save()
                form = Login()
                return render(request,"users/login.html",{'form':form})

            else:
                error = "Password does not matched.."
                form = Signup()
                return render(request,"users/signup.html",{'form':form,'error':error})
        else:
            error = "Invalid form"
            form = Signup()
            return render(request,"users/signup.html",{'form':form,'error':error})

def logout(request):
    del request.session['email']
    return redirect('/users/login/')
    #return render(request,"users/header.html")

def forgot(request):
    to_email = "tarun5585@gmail.com"
    from_email = "projectmail1601@gmail.com"
    subject = "Otp for password change"
    otp = randint(1000,9999)
    message = "One time otp for password change is {}".format(otp)
    send_mail(subject,message,from_email,(to_email,),auth_password=settings.EMAIL_HOST_PASSWORD)
    return HttpResponse("SUCCESS")
