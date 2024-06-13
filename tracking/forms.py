from django import forms
from .models import PhoneTracking


class PhoneTrackingForm(forms.ModelForm):
    class Meta:
        model = PhoneTracking
        fields = ['imei', 'phone_number']
