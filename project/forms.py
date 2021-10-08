from django.forms import ModelForm
from .models import Task

class CKEForm(ModelForm):

    class Meta:
        model = Task
        fields = ['remarks']