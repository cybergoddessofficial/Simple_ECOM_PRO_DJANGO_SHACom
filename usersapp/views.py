from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from adminapp.models import Product, Category


# Create your views here.
def base(request):
    data2= Category.objects.all()
    return render(request,"base.html", {'data2':data2})
def index(request):
    data = Product.objects.all()
    data2= Category.objects.all()
    return render(request,"users/index.html",{'data':data,'data2':data2})

def about(request):
    return render(request,"users/about.html")

def contact(request):
    return render(request,"users/contact.html")

def discat(request,itemcatname):
    data = Category.objects.all()
    catg=itemcatname.upper()
    products=Product.objects.filter(Cat=itemcatname)
    context={
        'products':products,
        'catg':catg,
        'data':data
    }
    return render(request,"users/categorydisplay.html",context)

def singlepro(request,sp):
    data=Product.objects.all()
    single=Product.objects.filter(Pro=sp)
    context={
        'data':data,
        'single':single
    }
    return render(request,"users/singlepro.html",context)

def registeruser(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        obj = User(username=uname,email=email,password=password)
        obj.save()
        return redirect(loginuser)
    return render(request,"users/register.html")

def loginuser(request):
    if request.method == "POST":
        username_r = request.POST.get("username")
        password_r = request.POST.get("password")
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username'] = username_r
                request.session['password'] = password_r
                return redirect(index)
            else:
                return redirect(loginuser)
    return render(request,"users/login.html")