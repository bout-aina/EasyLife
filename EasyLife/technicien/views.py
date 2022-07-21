
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .models import Technicien
import mysql.connector
from client.models import Offre
from client.models import Postuler
from django.contrib import messages 
from operator import itemgetter
from .forms import ProfileForm
from django.http import Http404, request


def register(request):
    if request.method == 'POST':
        user=Technicien()

        user.nom= request.POST['nom']
        user.prenom= request.POST['prenom']
        user.tel= request.POST['tel']
        user.ville= request.POST['ville']
        user.cin= request.POST['cin']
        user.domaine= request.POST['domaine']
        user.diplome= request.POST['diplome']
        user.email= request.POST['email']
        user.mdp= request.POST['mdp']
        user.save()
        messages.success(request,"New user registration details saved Successfully now try to login!")
        return render(request,"technicien/register-29.html")
    
    else:
        return render(request,"technicien/register-29.html")

def login(request):
    if request.method == 'POST':
        if Technicien.objects.filter(email=request.POST['email'] , mdp=request.POST['mdp']).exists():
            technicien = Technicien.objects.get(email=request.POST['email'] , mdp=request.POST['mdp'])
            request.session['email']=technicien.email
            return redirect("welcome")
        else:
            messages.success(request,"user or password invalid")
            return render(request,"technicien/login-29.html")

    else:
        return render(request,"technicien/login-29.html")


def welcome(request):
    if request.method == 'POST':
        obj = get_object_or_404(Technicien,email=request.session['email'])
        of = Offre.objects.all().filter(categorie__contains=request.POST['search'])
        context = {
        'object':obj,
        'of':of
        }
        return render(request,"technicien/welcome.html",context)
    else:
        obj = get_object_or_404(Technicien,email=request.session['email'])
        of = Offre.objects.all().filter(categorie=obj.domaine)
        context = {
        'object':obj,
        'of':of
        }
        return render(request,"technicien/welcome.html",context)

    
    
    
    
   

def logout(request):
    try:
        del request.session['email']
    except:
        return redirect("login")
    return redirect("login")

def profile(request):
    
    obj = get_object_or_404(Technicien,email=request.session['email'])
    
    context = {
        'object':obj
    }
    #print(context)
    return render(request,'technicien/profile.html',context)
    
def error(request):
    return render(request,'404.html')

def update(request):
    obj = Technicien.objects.get(email=request.session['email'])
    
    context = {
        'object':obj
    }
    if request.method == 'POST':  
        obj.nom= request.POST['nom']
        obj.prenom= request.POST['prenom']
        obj.tel= request.POST['tel']
        obj.ville= request.POST['ville']
        #technicien.cin= request.POST['cin']
        obj.domaine= request.POST['domaine']
        obj.diplome= request.POST['diplome']
        #technicien.email= request.POST['email']
        obj.mdp= request.POST['mdp']
        if request.POST['nom']=="" or request.POST['prenom']=="" or request.POST['tel']=="" or request.POST['ville']=="" or request.POST['domaine']=="" or request.POST['diplome']=="":
            messages.error(request,"Veuillez remplir tous les champs !")
            return redirect('update')
        else:
            obj.save()
            messages.success(request,"les informations ont été modifiées avec succès!")
            return redirect('update')
    else:
        return render(request,'technicien/update.html',context)

    
def destroy(request):  
    tec = get_object_or_404(Technicien,email=request.session['email'])
    tec.delete()  
    return redirect("login") 

def Detailsoffre(request,id):
    offre = Offre.objects.get(id=id)
    obj = Technicien.objects.get(email=request.session['email'])
    pos = Postuler.objects.all()
    dec=[]
   
    val=False
    
    if Postuler.objects.filter(offre_id=offre.id , technicien_id=obj.id).exists():
            #print("existe")
            val=True
    else:
            val=False
    
    if request.method == 'POST':
        pos=Postuler()
        pos.offre_id = offre.id
        pos.technicien_id = obj.id
        pos.save()
        messages.success(request,"Postulation avec succès")
        context ={ 
        'val':val,
        'pos':pos,
        'offre':offre,
        'object':obj
        }
        return redirect("postuler")
        
    else:   
            context ={
                'val':val,
                'offre':offre,
                'object':obj
                }
            return render(request,'technicien/details.html',context)



def postulation_page(request):
        
        obj = get_object_or_404(Technicien,email=request.session['email'])
        pos = Postuler.objects.all().filter(technicien_id=obj.id)
        context = {
        'object':obj,
        'pos':pos
        }
        return render(request,"technicien/postulation.html",context)

def destroy_postuler(request, id):  
    cl = Postuler.objects.get(id=id)  
    cl.delete()  
    return redirect("postuler") 