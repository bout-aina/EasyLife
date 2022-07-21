from django.shortcuts import render
from django.views import View
from .models import Contact_us
from django.contrib import messages 
class IndexView(View):
    def get(self,request):
        return render(request,"index.html")


def contact(request):
    if request.method == 'POST':
        user=Contact_us()

        user.nom= request.POST['name']
        user.email= request.POST['email']
        user.Message= request.POST['message']
        user.sujet= request.POST['subject']
        user.save()
        messages.success(request,"Votre est envoyé avec succès!")
        return render(request,"contact.html")
    
    else:
        return render(request,"contact.html")


    

def about(request):
    return render(request,"about.html")