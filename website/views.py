from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import FeedbackForm
from .models import FeedbackModel

def home(request):
    return render(request, 'website/home.html')

def feedback(request):
    if request.POST:
        form = FeedbackForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            contact = form.cleaned_data.get('contact')
            message = form.cleaned_data.get('message')

            feedback_model = FeedbackModel(name=name, contact=contact, message=message)
            feedback_model.save()

            empty_form = FeedbackForm()
            return render(request, 'website/feedback.html', {'feedback_form': empty_form})

    else:
        return redirect('home')

def aprender(request):
    return render(request, 'website/aprender.html')

def primeiros_passos(request):
    return render(request, 'website/primeiros-passos.html')

def primeira_camada(request):
    return render(request, 'website/primeira-camada.html')

def segunda_camada(request):
    return render(request, 'website/segunda-camada.html')

def terceira_camada(request):
    return render(request, 'website/terceira-camada.html')

def sobre_o_cubo_magico(request):
    return render(request, 'website/sobre-o-cubo-magico.html')

def avancado(request):
    return render(request, 'website/avancado.html')

