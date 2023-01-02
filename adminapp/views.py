from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


from adminapp.models import Student, Admin, Category, Product
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def adminindex(request):

    return render(request,"admin/index.html")

def addstudent(request):
    if request.method=="POST":
        Name = request.POST.get("fname")
        Email = request.POST.get("email")
        Gender = request.POST.get("gender")
        Image = request.FILES["pic"]
        City = request.POST.get("city")
        Address = request.POST.get("address")
        obj=Student(Name=Name,Email=Email,Gender=Gender,Image=Image,City=City,Address=Address)
        obj.save()
        return redirect(displaystudent)
    return render(request,"admin/addstudent.html")

def displaystudent(request):
    data=Student.objects.all()
    return render(request,"admin/displaystudent.html",{'data':data})

def editstudent(request,dataid):
    data = Student.objects.get(id=dataid)
    print(data)
    if request.method=="POST":
        Name = request.POST.get("fname")
        Email = request.POST.get("email")
        Gender = request.POST.get("gender")

        City = request.POST.get("city")
        Address = request.POST.get("address")
        try:
            Image = request.FILES['pic']
            fs=FileSystemStorage()
            file=fs.save(Image.name,Image)
        except MultiValueDictKeyError:
            file=Student.objects.get(id=dataid).Image
        Student.objects.filter(id=dataid).update(Name=Name,Email=Email,Gender=Gender,Image=file,City=City,Address=Address)
        return redirect(displaystudent)
    return render(request,"admin/editstudent.html",{'data':data})

def deletestudent(request,dataid):
    data = Student.objects.get(id=dataid)
    data.delete()
    return redirect(displaystudent)

def addadmin(request):
    if request.method=="POST":
        Name = request.POST.get("fname")
        Email = request.POST.get("email")
        Mobile = request.POST.get("mob")
        Image = request.FILES["pic"]
        Username = request.POST.get("username")
        Password = request.POST.get("password")
        CPassword = request.POST.get("cpassword")
        if Password==CPassword:
            obj = Admin(Name=Name, Email=Email, Mobile=Mobile, Image=Image, Username=Username, Password=Password,CPassword=CPassword)
            obj.save()
            return redirect(addadmin)
        else:
            messages.warning(request, 'Your password is mismatched.')



    return render(request,"admin/addadmin.html")

def displayadmin(request):
    data=Admin.objects.all()
    return render(request,"admin/displayadmin.html",{'data':data})

def editadmin(request,dataid):
    data = Admin.objects.get(id=dataid)
    if request.method=="POST":
        Name = request.POST.get("fname")
        Email = request.POST.get("email")
        Mobile = request.POST.get("mob")
        Username = request.POST.get("username")
        Password = request.POST.get("password")
        CPassword = request.POST.get("cpassword")
        try:
            Image = request.FILES['pic']
            fs=FileSystemStorage()
            file=fs.save(Image.name,Image)
        except MultiValueDictKeyError:
            file=Admin.objects.get(id=dataid).Image
        if Password == CPassword:
            Admin.objects.filter(id=dataid).update(Name=Name, Email=Email, Mobile=Mobile, Image=file, Username=Username, Password=Password,
                        CPassword=CPassword)
            return redirect(displayadmin)
        else:
            messages.warning(request, 'Your password is mismatched.')
    return render(request,"admin/editadmin.html",{'data':data})

def deleteadmin(request,dataid):
    data = Admin.objects.get(id=dataid)
    data.delete()
    return redirect(displayadmin)

def addcategory(request):
    if request.method=="POST":
        CName=request.POST.get("cname")
        CDesc=request.POST.get("cdesc")
        CImage=request.FILES["pic"]
        obj=Category(CName=CName,CDesc=CDesc,CImage=CImage)
        obj.save()
        return redirect(displaycategory)
    return render(request,"admin/addcategory.html")

def displaycategory(request):
    data=Category.objects.all()
    return render(request,"admin/displaycategory.html",{'data':data})

def editcategory(request,dataid):
    data = Category.objects.get(id=dataid)
    if request.method=="POST":
        CName = request.POST.get("cname")
        CDesc = request.POST.get("cdesc")
        try:
            Image = request.FILES['pic']
            fs=FileSystemStorage()
            file=fs.save(Image.name,Image)
        except MultiValueDictKeyError:
            file=Category.objects.get(id=dataid).CImage
        Category.objects.filter(id=dataid).update(CName=CName,CDesc=CDesc,CImage=file)
        return redirect(displaycategory)
    return render(request,"admin/editcategory.html",{'data':data})

def deletecategory(request,dataid):
    data = Category.objects.get(id=dataid)
    data.delete()
    return redirect(displaycategory)


def addproduct(request):
    data=Category.objects.all()
    if request.method=="POST":
        Cat=request.POST.get("category")
        Pro=request.POST.get("pname")
        Price=request.POST.get("price")
        Quantity=request.POST.get("quantity")
        Desc=request.POST.get("pdesc")
        Image=request.FILES["pic"]
        obj=Product(Cat=Cat,Pro=Pro,Price=Price,Quantity=Quantity,Desc=Desc,Image=Image)
        obj.save()
        return redirect(displayproduct)
    return render(request,"admin/addproduct.html",{'data':data})

def displayproduct(request):
    data=Product.objects.all()
    return render(request,"admin/displayproduct.html",{'data':data})

def editproduct(request,dataid):
    data = Product.objects.get(id=dataid)
    data2 = Category.objects.all()
    if request.method == "POST":
        Cat = request.POST.get("category")
        Pro = request.POST.get("pname")
        Price = request.POST.get("price")
        Quantity = request.POST.get("quantity")
        Desc = request.POST.get("pdesc")
        try:
            Image = request.FILES['pic']
            fs = FileSystemStorage()
            file = fs.save(Image.name, Image)
        except MultiValueDictKeyError:
            file = Product.objects.get(id=dataid).Image
        Product.objects.filter(id=dataid).update(Cat=Cat,Pro=Pro,Price=Price,Quantity=Quantity,Desc=Desc,Image=file)
        return redirect(displayproduct)
    return render(request, "admin/editproduct.html", {'data': data,'data2':data2})


def deleteproduct(request,dataid):
    data = Product.objects.get(id=dataid)
    data.delete()
    return redirect(displayproduct)


def adminlogin(request):
    if request.method=="POST":
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(adminindex)
            else:
                return redirect(adminlogin)
        else:
            return redirect(adminlogin)
    return render(request,"admin/adminlogin.html")

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)



