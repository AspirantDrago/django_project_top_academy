from django.shortcuts import render, redirect
from .models import History
from .forms import HistoryForm

# Create your views here.

def index(request):
    historyes = History.objects.all()
    context = {
        'historyes':historyes
    }
    return render(request, 'history/index.html', context)



def create(request):
    if request.POST:
        form = HistoryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('history')
    form = HistoryForm()
    context = {
        'form':form,
    }
    return render(request, 'history/create.html', context)

def show(request, pk):
    try:
        history = History.objects.get(id=pk)
        context = {}
        context.update({'history':history})
        return render(request, 'history/index.html', context)
    except:
        return redirect('histories:index')



