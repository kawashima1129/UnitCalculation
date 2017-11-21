from django.shortcuts import render, get_object_or_404, redirect
from .forms import TimeTableForm
from .models import Unit

# Create your views here.

def index(request):
    print(request.method)
    if request.method == 'POST':
        form = TimeTableForm(data = request.POST)
        if form.is_valid():
            form.calc()
            return redirect('calc:results')
    else:
        form = TimeTableForm()
    return render(request, 'calc/index.html', {'form':form})

def results(request):
    return render(request, 'calc/results.html')
