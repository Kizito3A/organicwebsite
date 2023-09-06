from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def home(request):
     return render(request, "index.html", {})

def contact(request):
     if request.method == 'POST':
          form = ContactForm()
     else:
          form = ContactForm(request.POST)
          if form.is_valid():
               name = form.cleaned_data['name']
               email = form.cleaned_data['email']
               message = form.cleaned_data['message']
               phone  = form.cleaned_data['phone']
               try:

                  send_mail(name, email,message,phone, ['kizitoamandi90@gmail.com'])
               except BadHeaderError:
                  return HttpResponse("Invalid header found.")
               return redirect('contact.html')
     return render(request, 'contact.html', {'form':form})



def activity(request):

     return render(request, "about.html", {})

def products(request):

     return render(request, "products.html", {})

def about(request):

     return render(request, "about.html", {})





