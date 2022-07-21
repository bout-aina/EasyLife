from django.forms import ModelForm
from .models import Technicien



class ProfileForm(ModelForm):
    class Meta:
        model=Technicien
        fields=('nom','prenom','email','tel','ville','cin','domaine','diplome')