from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from orchids.models import Orchid, Greenhouse


class NumberForm(forms.Form):
    number = forms.IntegerField(label='Number of days to simulate', initial=1,
                                validators=[MinValueValidator(0), MaxValueValidator(20)])


class OrchidForm(forms.ModelForm):
    class Meta:
        model = Orchid
        fields = ['name', 'preferred_weather', 'original_days_in_andes',
                  'original_days_in_coast', 'number', 'min_temperature', 'max_temperature', ]
        labels = {
            "name": "Identifier",
            "original_days_in_andes": "Number of days in andes",
            "original_days_in_coast": "Number of days in coast"
        }

        help_texts = {
            'name': 'alphanumeric identifier for the orchid batch',
            'number': 'number of plants in the batch',
            'min_temperature': 'min recommended temperature',
            'max_temperature': 'max recommended temperature',
        }


class GreenhouseForm(forms.ModelForm):
    class Meta:
        model = Greenhouse
        fields = ['name', 'weather', 'temperature', 'capacity', ]
        labels = {
            "name": "Identifier",
        }

        help_texts = {
            'name': 'alphanumeric identifier for the greenhouse',
            'capacity': 'Number of plants that fit the greenhouse',
        }
