from django import forms
from .models import Villa


class VillaUpdateForm(forms.ModelForm):
    class Meta:
        model = Villa
        fields = (
            'category',
            'image',
            'area',
            'material',
            'security',
            'description',
            'floor_number',
            'bedroom',
            'bathroom',
            'parking_space_capacity',
            'price',
            'payment_method',
            'address',
            'zip_code',
            'region',
            'is_active',
        )
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
            'security': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'floor_number': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'bedroom': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'bathroom': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'parking_space_capacity': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
