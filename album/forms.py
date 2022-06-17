from django import forms
from .models import DateIdeas

class LookDate(forms.ModelForm):
    class Meta:
        model = DateIdeas
        fields = ('title',)

class DateForm(forms.ModelForm):
    class Meta:
        model = DateIdeas
        fields = ('title', 'details', 'priority', 'duration',)
        widgets = {
         'priority': forms.TextInput(attrs={'type': 'range', 'min': "0", 'max':"10", 'step':"1"})
         }


class DateEditForm(forms.ModelForm):
    class Meta:
        model = DateIdeas
        fields = ('title', 'check_done', 'review', 'image', 'date_done',)
    
