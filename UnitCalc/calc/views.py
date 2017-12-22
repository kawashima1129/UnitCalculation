from django.shortcuts import render, get_object_or_404, redirect
from .forms import TimeTableForm, ContactForm
from .models import Unit
from django.utils.html import mark_safe

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = TimeTableForm(data = request.POST)
        request_dict = dict(request.POST)
        if form.is_valid():
            summary = form.calc(request_dict['unit'])
            return render(request, 'calc/results.html', summary)
    else:
        form = TimeTableForm()
        form = form.shaping(form)
        return render(request, 'calc/index.html', {'form':mark_safe(form)})


def inquire(request):
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.send_email()
            return render(request, 'calc/inquire.html', 
                          {'form':form, 'true':'Your message is submitted. Thank you!'})
    else:
        form = ContactForm()
    return render(request, 'calc/inquire.html', {'form':form})


