from technicien.models import Technicien
import client
from django.shortcuts import render,redirect,HttpResponseRedirect
from client.models import Client, Offre, Postuler , Message 
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
import datetime
from django.http.response import HttpResponse, JsonResponse
import json
from django.db.models import Q
from django.core import serializers


def homeLogin(request):
    if request.method == 'POST':
        if Client.objects.filter(email=request.POST.get('email'),mdp=request.POST.get('password')).exists():
            client = Client.objects.get(email=request.POST.get('email'),mdp=request.POST.get('password'))
            request.session['email']=client.email
            return redirect("profile_client")
        else:
            message = messages.success(request,"le mot de passe ou l'email incorrecte")
            return render(request,"login_client.html",message)
    else:
        return render(request,"login_client.html")

def registerPage(request):
    if request.method == 'POST':
        client = Client(nom=request.POST.get('nom'),prenom=request.POST.get('prenom'),email=request.POST.get('email'),mdp=request.POST.get('password'),tel=request.POST.get('tel'),ville=request.POST.get('ville'))
        client.save()
        return redirect('login_Client')
    
    else:
        return render(request,'register_client.html')
    
def getDetailClient(request):
        client = get_object_or_404(Client,email=request.session['email'])
        context = {'data':client}
        return render(request,'client/profile_client.html',context)

def modifierClient(request):
    client = get_object_or_404(Client,email=request.session['email'])
    context = {
        'data':client,
    }
    if request.method =='POST':
        client = Client.objects.get(email=request.session['email'])
        client.nom = request.POST['nom']
        client.prenom = request.POST['prenom']
        client.tel = request.POST['tel']
        client.ville = request.POST['ville']
        if request.POST['new']:
            client.mdp = request.POST['new']
        client.save()
        return redirect("profile_client")
    return render(request,'client/modifier_client.html',context)

def GetAllOffre(request):
    if request.method == 'POST':
        client1 = Client.objects.get(email=request.session['email'])
        offre = Offre(date_pub=datetime.datetime.now(),description=request.POST['description'],categorie=request.POST['categorie'],client=client1)
        offre.save()
        return redirect('list_offre')
    offre = Offre.objects.all()
    return render(request,"client/List_offre.html",{'offre':offre})

def GetDetailsOffre(request,idC):
    offre = Offre.objects.get(id=idC)
    return render(request,'client/Details_offre.html',{'offre':offre})

def GetOffreClient(request):
    client1 = Client.objects.get(email=request.session['email'])
    offre = Offre.objects.all().filter(client=client1)
    return render(request,'client/Offre_client.html',{'offre':offre})

def ModifierOffre(request,idO):
    offre = Offre.objects.get(id=idO)
    if request.method == 'POST':
        offre.categorie = request.POST.get('categorie')
        offre.description = request.POST.get('description')
        offre.save()
        return redirect('offre_by_client')
    return render(request,'client/modifier_offre.html',{'offre':offre})

def LogOut(request):
    try:
        del request.session['email']
    except:
        return redirect("login_Client")
    return redirect("login_Client")

def DeleteClient(request):
    client = Client.objects.get(email=request.session['email'])
    client.delete()
    return redirect("login_Client")

def DeleteOffre(request,idO):
    offre = Offre.objects.get(id=idO)
    offre.delete()
    return redirect("offre_by_client")

def GetListPostuler(request,idO):
    postuler = Postuler.objects.all().filter(offre_id=idO)
    if postuler :
        return render(request,"client/liste_postuler.html",{'postuler':postuler})
    else:
        erreur =1 
        return render(request,"client/liste_postuler.html",{'erreur':erreur})

# def chatroom(request,idT):
#      technicien = Technicien.objects.get(id=idT)
#      client = Client.objects.get(email=request.session['email'])
#      message = Message.objects.filter(
#          Q(technicien=technicien,client=client)
#      )
#      return render(request,"client/chatroom.html",{"technicien":technicien,"message":message, "client":client})

# # def ajax(request,idT):
#     technicien = Technicien.objects.get(id=idT)
#     client = Client.objects.get(email=request.session['email'])
#     message = Message.objects.filter(
#          Q(technicien=technicien,client=client)
#     )

#     message_list=[]
#     for m in message:
#         message_list.append({
#             "client":m.client.__str__(),
#             "message":m.message,
#             "technicien":m.technicien.__str__(),
#             "sentBy":m.sentBy
#         })
    
#     if request.method == "POST":
#         message = json.loads(request.body)
#         m = Message(technicien=technicien,client=client,message=message,sentBy="c")
#         message_list.append({
#             "client":m.client.__str__(),
#             "message":m.message,
#             "technicien":m.technicien.__str__(),
#             "sentBy":m.sentBy
#         })
        
#     #ajax_message = serializers.serialize("json",message_list)
#     #return JsonResponse(ajax_message,safe=False)
#     return HttpResponse( json.dumps(message_list),content_type='application/json')