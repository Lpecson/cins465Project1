from django.shortcuts import render

# Create your views here.
def BudgetMain(request):
    return render(request, 'budget/home.html')
