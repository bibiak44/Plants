"""
Definition of forms.
"""

from django import forms
from .models import Plant1
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class PlantForm(forms.ModelForm):

    typ = forms.ModelChoiceField(queryset=Plant1.objects.values_list('typ', flat=True).distinct())
    farba = forms.ModelChoiceField(queryset=Plant1.objects.values_list('farba', flat=True).distinct())
    pouzitie = forms.ModelChoiceField(queryset=Plant1.objects.values_list('pouzitie', flat=True).distinct())
    stanovisko = forms.ModelChoiceField(queryset=Plant1.objects.values_list('stanovisko', flat=True).distinct())
    slnko = forms.ModelChoiceField(queryset=Plant1.objects.values_list('slnko', flat=True).distinct())
    vlaha = forms.ModelChoiceField(queryset=Plant1.objects.values_list('vlaha', flat=True).distinct())

    class Meta:
        model = Plant1
        fields = ["farba", "typ", "pouzitie", "stanovisko", "slnko", "vlaha"]