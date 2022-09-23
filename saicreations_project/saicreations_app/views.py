from django.shortcuts import render,redirect
from .models import Newsletter, Product, Admin
from django.contrib import messages
from passlib.hash import sha512_crypt as sha512

# Create your views here.
def index(request):
    return render(request, 'index.html')

def add_to_newsletter(request):
    email = request.POST['email']
    Newsletter.objects.create(email=email)
    return redirect('index')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def login_admin(request):
    email = request.POST["email"]
    password = request.POST["pwd"]
    pwd = sha512.hash(password, rounds=5000,salt="anamikasehgal")
    print(pwd)
    admi = Admin.objects.filter(email=email)
    for x in admi:
        print(x.password)
    if Admin.objects.filter(email=email, password=pwd).exists():
        request.session['AnamikaSehgalPrivateKey']="Thisisaprivatekeynotsupposedtobeknownbyyou"
        return redirect('admin')
    print("wrong")
    messages.info(request, 'Invalid Credentials')
    return redirect('admin_login')

def admin(request):
    if 'AnamikaSehgalPrivateKey' in request.session:
        if request.session['AnamikaSehgalPrivateKey'] == "Thisisaprivatekeynotsupposedtobeknownbyyou":
            return render(request, 'admin.html')
        else:
            return redirect('admin_login')
    return redirect('admin_login')

def addproductpage(request):
    if 'AnamikaSehgalPrivateKey' in request.session:
        if request.session['AnamikaSehgalPrivateKey'] == "Thisisaprivatekeynotsupposedtobeknownbyyou":
            return render(request, 'admin_add_product.html')
        else:
            return redirect('admin_login')
    return redirect('admin_login')

def adminseeorders(request):
    if 'AnamikaSehgalPrivateKey' in request.session:
        if request.session['AnamikaSehgalPrivateKey'] == "Thisisaprivatekeynotsupposedtobeknownbyyou":
            return render(request, 'admin_orders.html')
        else:
            return redirect('admin_login')
    return redirect('admin_login')