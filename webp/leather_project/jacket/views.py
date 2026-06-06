from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import JacketForm
from .models import Jacket


def addJacket(request):
    if request.method == 'POST':
        form = JacketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'message.html', {'msg': 'Jacket Added Successfully'})
    else:
        form = JacketForm()

    return render(request, 'add.html', {'form': form})


def showAll(request):
    data = Jacket.objects.all()
    return render(request, 'show.html', {'data': data})


def delete(request):
    id = request.GET['id']
    Jacket.objects.get(j_id=id).delete()
    return redirect('/show/')


def update(request):
    id = request.GET['id']
    obj = Jacket.objects.get(j_id=id)

    if request.method == 'POST':
        form = JacketForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/show/')
    else:
        form = JacketForm(instance=obj)

    return render(request, 'update.html', {'form': form})