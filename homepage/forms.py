from django.forms import ModelForm
from .models import Participant 

class RegistrationForm(ModelForm):
    class Meta:
       model=Participant
       fields=['email']