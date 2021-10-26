from django.shortcuts import render

# Create your views here.
def TasksMain(request):
    return render(request, 'tasks/home.html')
