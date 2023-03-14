from django.shortcuts import render

from .utils.calculator import calculator
from .forms import CalculatorForm


def calculate_savings(request):
    form = CalculatorForm()

    if request.method == "POST":
        form = CalculatorForm(request.POST)
        if form.is_valid():
            consumption = [
                float(request.POST["consumption1"]),
                float(request.POST["consumption2"]),
                float(request.POST["consumption3"]),
            ]
            distributor_tax = float(request.POST["distributor_tax"])
            tax_type = request.POST["tax_type"]
            savings = calculator(consumption, distributor_tax, tax_type)
            context = {
                "savings": savings,
            }
            return render(request, "savings.html", context)
        
    context = {
        'form': form,
    }

    return render(request, "calculate_savings.html", context)
