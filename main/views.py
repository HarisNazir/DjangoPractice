from django.shortcuts import render
from .forms import GetCountry, UploadExcel
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import requests
from .generatefile import generateExcelFile, download_file
import json
from .ExcelToModel import AddToModel
from django.views.generic.edit import FormView



def GetCountryCode(request):
    if request.method == 'GET':
        form = GetCountry()
        return render(request, "getcountry.html", {'form': form})
    elif request.method == 'POST':
        form = GetCountry(request.POST)
        if form.is_valid():
            iso_code = form.cleaned_data['iso3']
            return GenerateExcel(iso_code)
    
def GenerateExcel(iso_code):
    res = requests.get(f"https://restcountries.eu/rest/v2/alpha/{iso_code}")
    data = res.json()
    generateExcelFile(data)
    return download_file()
    
def UploadFile(request):
    if request.method == 'GET':
        form = UploadExcel()
        return render(request, "fileupload.html", {'form': form})
    elif request.method =='POST':
        breakpoint()
        form = UploadExcel(request.POST, request.FILES)
        
        if form.is_valid():
            AddToModel(form.cleaned_data['file'])
            return HttpResponse("Data Added")
        else:
            return render(request, "fileupload.html", {'form': form})

class UploadScreen(FormView):
    template_name = "fileupload.html"
    form_class = UploadExcel
    success_url = "/"

    def form_valid(self, form):
        AddToModel(form.cleaned_data)
