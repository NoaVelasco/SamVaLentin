from random import choice
from django.shortcuts import render, redirect, get_object_or_404
from .models import Personas
from .forms import PersonasForm


# Create your views here.
def home(request):
    if request.method == "POST":
        form = PersonasForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid():
            name = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            name.save()
            return redirect("home")
    else:
        form = PersonasForm()
    return render(request, "formulario/home.html", {"form": form})



def results(request):
    entradas = Personas.objects.all()
    if entradas:
        nombre = choice(entradas)
        nombre = nombre.name
        Personas.objects.filter(name=nombre).delete()
        return render(request, "formulario/results.html", {'nombre': nombre})
    else:
        return render(request, "formulario/results.html", {'nombre': "No quedan nombres."})
    
def reset(request):
    try:
        Personas.objects.delete()
    except:
        pass
    return render(request, "formulario/results.html", {'nombre': "No quedan nombres."})


