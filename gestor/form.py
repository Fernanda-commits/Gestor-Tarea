from .models import Tarea
from django.forms import ModelForm

class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'