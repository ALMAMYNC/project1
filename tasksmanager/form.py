# taches/forms.py
from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'dateE', 'status']

    Date_echeance = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    STATUT_CHOICES = [
        ('', 'Tous'),  
        ('1', 'Terminées'),
        ('0', 'Non terminées'),
    ]
    statut = forms.ChoiceField(choices=STATUT_CHOICES, required=False)

   
class TaskDeleteForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = []  

class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'dateE', 'status']
