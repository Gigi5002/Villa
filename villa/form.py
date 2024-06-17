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
