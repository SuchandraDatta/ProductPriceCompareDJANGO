from django.shortcuts import render
from .models import Articles
from .forms import NameForm
from .myWebScraping import startScraping
from django.http import HttpResponseRedirect
from django.urls import reverse
def article_list(request):
    articlesVar=Articles.objects.all().order_by('date')
    return render(request,'articles/articles_list.html', {'articles':articlesVar})

def submitted(request):
    return render(request, 'articles/form_submitted.html')

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            priceList=[]
            itemName=form.cleaned_data['your_name']
            companyName=form.cleaned_data['your_company']
            modelNumber=form.cleaned_data['your_modelNumber']
            print("ITEM NAME: ", itemName, "\nCOMPANY NAME: ", companyName, "\nMODEL NUMBER: ", modelNumber)
            priceList=startScraping(itemName, companyName, modelNumber)
            return render(request, 'articles/form_submitted.html', {'itemName':itemName, 'companyName':companyName, 
            'modelNumber': modelNumber, 'amazonPrice':priceList[0], 'flipkartPrice': priceList[1], 'ebayPrice': priceList[2]})
            #return HttpResponseRedirect('http://127.0.0.1:8000/articles/submitted')
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'articles/name.html', {'form': form})

