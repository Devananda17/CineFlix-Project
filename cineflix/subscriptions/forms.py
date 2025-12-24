from django import forms

from .models import SubscriptionPlans

import os

class SubscriptionForm(forms.ModelForm):

    class Meta :

        model = SubscriptionPlans

        exclude = ['uuid','active_status']

        widgets = {

          'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter plan name'}),

          'amount':forms.NumberInput(attrs={'class':'form-control'}),

          'devices':forms.SelectMultiple(attrs={'class':'form-control'}),

          'quality':forms.Select(attrs={'class':'form-control'}),

          'no_of_screens':forms.Select(attrs={'class':'form-control'}),

          'download_devices':forms.Select(attrs={'class':'form-control'})
          
        }

        def clean(self):
           
           cleaned_data = super().clean()
