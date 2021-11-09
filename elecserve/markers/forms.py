from django import forms
from .json_schema import validate_markerpack
import json
from .models import Category

class MarkersForm(forms.Form):
    data = forms.FileField(label="Marker pack")
    category = forms.ModelChoiceField(label="Category",queryset=Category.objects.all())

    def get_json(self):
        data = self.cleaned_data['data']
        data.seek(0)
        jdata = json.load(data)
        return jdata

    def clean_data(self):
        try:
            validate_markerpack(self.get_json())
        except Exception as e:
            raise forms.ValidationError("Error validating marker pack: " + str(e))
        return self.cleaned_data['data']