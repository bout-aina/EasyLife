from base.models import Contact_us
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Chef
import mysql.connector
from technicien.models import Technicien 
from client.models import Client,Offre

from django.contrib import messages 
# Create your views here.
def login_admin(request):
    if request.method == 'POST':
        if Chef.objects.filter(email=request.POST['email'] , mdp=request.POST['mdp']).exists():
            admine = Chef.objects.get(email=request.POST['email'] , mdp=request.POST['mdp'])
            request.session['email']=admine.email
            return redirect('welcome_admin')
        else:
            messages.success(request,"user or password invalid")
            return render(request,"_admin/login.html")

    else:
        return render(request,"_admin/login.html")

def welcome_admin(request):
    if request.method == 'POST':
        tec = Technicien.objects.all().filter(nom__contains=request.POST['search'] )
        return render(request,"_admin/welcome.html",{'tec':tec}) 
    else:
        tec = Technicien.objects.all()  
        return render(request,"_admin/welcome.html",{'tec':tec}) 

def welcome_client(request):
    if request.method == 'POST':
        cl = Client.objects.all().filter(nom__contains=request.POST['search'] )
        return render(request,"_admin/client.html",{'cl':cl}) 
    else:
        cl = Client.objects.all()  
        return render(request,"_admin/client.html",{'cl':cl}) 

def welcome_contact(request):
    if 'search' in request.GET:
        search=request.GET['search']
        co = Contact_us.objects.all().filter(nom__contains=search)
        context ={
         'co':co
        }
        return render(request,"_admin/contact_us.html",context) 
    else:
        co = Contact_us.objects.all()
        return render(request,"_admin/contact_us.html",{'co':co}) 
   

def welcome_offre(request):
    if request.method == 'POST':
        of = Offre.objects.all().filter(categorie__contains=request.POST['search'] )
        return render(request,"_admin/offre.html",{'of':of}) 
    else:
        of = Offre.objects.all()  
        return render(request,"_admin/offre.html",{'of': of}) 
    
    

def logout_admin(request):
    try:
        del request.session['email']
    except:
        return redirect("login_admin")
    return redirect("login_admin")

def destroy(request, id):  
    tec = Technicien.objects.get(id=id)  
    tec.delete()  
    return redirect("welcome_admin") 

def destroy_client(request, id):  
    cl = Client.objects.get(id=id)  
    cl.delete()  
    return redirect("client") 

def destroy_offre(request, id):  
    of = Offre.objects.get(id=id)  
    of.delete()  
    return redirect("offre") 

def destroy_contact(request, id):  
    co = Contact_us.objects.get(id=id)  
    co.delete()  
    return redirect("contact_admin") 

# def searchbar(request):
#     if 'search' in request.GET:
#         search=request.GET['search']
#         tec=Technicien.objects.all().filter(title__icontains=search)
#         return redirect('')
#     else:
#         tec = Technicien.objects.all()  
#         return render(request,"_admin/welcome.html",{'tec':tec})


        
