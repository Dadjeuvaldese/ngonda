from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .forms import ContactForm, ParagraphErrorList

def home(request):
    
    if request.method == 'POST' :
        form = ContactForm(request.POST, error_class = ParagraphErrorList)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email'] 
            message = form.cleaned_data['message']
            form.save() 
        # return redirect('users/home.html')

    else :
        form = ContactForm()   

    return render(request, "users/home.html", {'form':form})     
  