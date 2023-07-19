from django import forms
   
# import GeeksModel from models.py
from api import models as api
   
# create a ModelForm
class DepartmentForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = api.Department
        fields = "__all__"