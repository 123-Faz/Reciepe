from django.shortcuts import render, redirect
from .models import Reciepe
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def Reciepe1(request):
    if request.method == 'POST':
        Reciepe_name = request.POST.get('Reciepe_name')
        Reciepe_description = request.POST.get('Reciepe_description')
        Reciepe_image = request.FILES.get('Reciepe_image')

        Reciepe.objects.create(
        Reciepe_name = Reciepe_name,
        Reciepe_description = Reciepe_description,
        Reciepe_image = Reciepe_image,
        )
        
        return redirect('/Reciepe1/')
    
    
    queryset = Reciepe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(Reciepe_name__icontains = request.GET.get('search'))

    context = {'Reciepe1': queryset}
    
    return render(request, 'reciepe.html', context)


@login_required()
def deleterp(request, id):
    queryset = Reciepe.objects.get(id=id)
    queryset.delete()
    return redirect('/Reciepe1/')

@login_required()
def updaterp(request, id):
    queryset = Reciepe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        
        Reciepe_name = request.POST.get('Reciepe_name')
        Reciepe_description = request.POST.get('Reciepe_description')
        Reciepe_image = request.FILES.get('Reciepe_image')

        queryset.Reciepe_name = Reciepe_name
        queryset.Reciepe_description = Reciepe_description

        if Reciepe_image:
            queryset.Reciepe_image = Reciepe_image
        
        queryset.save()
        return redirect('/Reciepe1/')
 

    context = {'reciepe': queryset}
    return render(request, 'updaterp.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

 
        if not User.objects.filter(username =  username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login/')


        user =  authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect('/login/')

        else:
            login(request, user)
            return redirect('/Reciepe1/')
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username =  username)
        if user.exists():
            messages.info(request, "the username is already taken")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,   
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account Created successfully")
           

        return redirect('/login/')
        
    return render(request, 'register.html')