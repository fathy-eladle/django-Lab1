from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Trainee

from django.contrib.auth.decorators import login_required

@login_required
def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})



from django.shortcuts import render, redirect
from .models import Trainee
from .forms import TraineeForm

@login_required
def add_trainee(request):
    if request.method == "POST":
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm()
    return render(request, 'trainee/add_trainee.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from .forms import TraineeForm
@login_required
def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/trainee_list.html', {'trainees': trainees})

@login_required
def add_trainee(request):
    if request.method == "POST":
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm()
    return render(request, 'trainee/add_trainee.html', {'form': form})

@login_required
def update_trainee(request, trainee_id):
    trainee = get_object_or_404(Trainee, id=trainee_id)
    if request.method == "POST":
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('trainee_list')
    else:
        form = TraineeForm(instance=trainee)
    return render(request, 'trainee/update_trainee.html', {'form': form})

@login_required
def delete_trainee(request, trainee_id):
    trainee = get_object_or_404(Trainee, id=trainee_id)
    if request.method == "POST":
        trainee.delete()
        return redirect('trainee_list')
    return render(request, 'trainee/delete_trainee.html', {'trainee': trainee})
