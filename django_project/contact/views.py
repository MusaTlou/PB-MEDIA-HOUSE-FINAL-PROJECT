# contact/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
          

            # Save data to the database or send an email, etc.
            # For this example, we'll just return a success response
            return HttpResponse("Thank you for your message.")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
