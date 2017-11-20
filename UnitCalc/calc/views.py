from django.shortcuts import render, get_object_or_404
from .forms import TimeTableForm
from .models import Unit

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = TimeTableForm(data = request.POST)
    else:
        form = TimeTableForm()
    return render(request, 'calc/index.html', {'form':form})
