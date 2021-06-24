from django.shortcuts import render
from .forms import GetCountry
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def GetCountryCode(request):
    form = GetCountry()
    return render(request, "getcountry.html", {'form': form})

def GenerateExcel(request):
    file =
        
