from django.forms import ModelForm
from . import models

class productoForm(ModelForm):
    class Meta:
        model = models.Producto
        fields = '__all__'