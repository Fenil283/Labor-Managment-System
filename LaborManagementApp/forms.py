from django import forms
from LaborManagementApp.models import Laborer,Supervisor


class LaborerForms(forms.ModelForm):
    class Meta:
        model = Laborer
        fields = "__all__"

class SupervisorForms(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = "__all__"
