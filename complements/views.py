from django.shortcuts import render, redirect
from .forms import DocumentForm

# Create your views here.
def model_correction(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'complements/model_correction.html', {
        'form': form
    })