from django import forms

class CalculatorForm(forms.Form):
    consumption1 = forms.FloatField(label="Consumption 1")
    consumption2 = forms.FloatField(label="Consumption 2")
    consumption3 = forms.FloatField(label="Consumption 3")
    distributor_tax = forms.FloatField(label="Distributor Tax")
    tax_type_choices = [
        ("Residencial", "Residencial"),
        ("Comercial", "Comercial"),
        ("Industrial", "Industrial"),
    ]
    tax_type = forms.ChoiceField(
        label="Tax Type",
        widget=forms.Select,
        choices=tax_type_choices,
    )