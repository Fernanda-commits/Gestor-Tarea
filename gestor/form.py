from models import Tarea
from django.forms import modelform

class TareaForm(modelform):
    class Meta:
        model = Tarea
        fields = '__all__'