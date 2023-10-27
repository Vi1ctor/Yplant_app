from django import forms
from django.contrib.auth.models import User

class HomeForm(forms.Form):
    N = forms.FloatField(
        label='Nível de nitrogênio',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0', 'name': 'N'})
    )
    P = forms.FloatField(
        label='Nível de fósforo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0', 'name': 'P'})
    )
    K = forms.FloatField(
        label='Nível de Potássio',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0', 'name': 'K'})
    )
    temperature = forms.FloatField(
        label='Temperatura',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0', 'name': 'temperature'})
    )
    humidity = forms.FloatField(
        label='Umidade',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0', 'name': 'humidity'})
    )
    soil_ph = forms.FloatField(
        label='pH do solo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0', 'name': 'soil_ph'})
    )
    water_per_year = forms.FloatField(
        label='Água disponível por ano',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0', 'name': ' water_per_year'})
    )
    rainfall = forms.FloatField(
        label='Precipitação',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '0', 'name': 'rainfall'})
    )

class FilterForm(forms.Form):
    start_date = forms.DateField(
        label='Data Inicial',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=False  # O campo não é obrigatório
    )
    
    end_date = forms.DateField(
        label='Data Final',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=False  # O campo não é obrigatório
    )
    
    plantation_name = forms.CharField(
        label='Nome da Plantação',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False  # O campo não é obrigatório
    )

    class LoginForm(forms.Form):
        username= forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)

