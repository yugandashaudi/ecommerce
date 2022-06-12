from .models import ShipppingInformation
from django import forms

class shippingdetails(forms.ModelForm):
    class Meta:
        model = ShipppingInformation
        fields ='__all__'