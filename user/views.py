from . forms import RegisterForm,LoginForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def register(request):

    form=RegisterForm(request.POST or None)

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.info(request,"Başarıyla Kayıt Oldunuz...")
        return redirect("index")

    context={
            "form":form
        }
    return render(request,"register.html",context)

  
    



def LoginUser(request):

    form=LoginForm(request.POST or None)

    context={
            "form":form
        }

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        User=authenticate(username=username,password=password)

        if User is None:
            messages.info(request,"Kullanıcı Adı veya Paralo Hatalıdır.")
            return render(request,"login.html",context)
        
        messages.success(request,"Başarıyla Giriş Yaptınız..")
        login(request,User)
        return redirect("index")

    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız..")
    return redirect("index")