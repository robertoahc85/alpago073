# school/forms.py
from django import forms
from .models import School

class SchoolAdminForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'
        widgets = {
            'institution_type': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'education_level': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'education_modality': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'shifts': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }