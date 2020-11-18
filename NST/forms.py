from django import forms 
from .models import NstImages
  
class NstImagesForm(forms.ModelForm): 
    
    class Meta: 
        model = NstImages
        fields = ['content','style'] 
