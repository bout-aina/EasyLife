from django.contrib import admin

# Register your models here.
from .models import Client
from .models import Offre,Postuler
admin.site.register(Client)
admin.site.register(Offre)
admin.site.register(Postuler)