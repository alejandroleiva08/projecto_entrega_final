from django.shortcuts import render
#from .models import Cliente

# Create your views here.
def index(request):
    return render(request, "CORE/index.html")
