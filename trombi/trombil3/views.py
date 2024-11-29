from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Personne, Formation, Experience, Competence

"""def index(requset , *args, **kwargs):
    personne=Personne.objects.all()
    for personne in queryset:
        context={
        'nom':personne.nom ,
        'prenom':personne.prenom,
        'telephone':personne.telephone,
        'mail':personne.mail,
        'photo':personne.photo
    }
    return render(requset, "detail.html",context)"""
def acceuil(request):
    return HttpResponse("<h1>BIENVUE SUR MON TROMINOSCOPE</h1>")

def index(request):
    personnes = Personne.objects.all()  # Récupère un QuerySet de toutes les personnes
    context = []  # On crée une liste vide pour stocker les données de chaque personne
    
    for personne in personnes:
        context.append({
            'nom': personne.nom,
            'prenom': personne.prenom,
            'telephone': personne.telephone,
            'mail': personne.mail,
            'photo': personne.photo
        })

    return render(request, "index.html", {'personnes': context})
def detail(request):
    personne_object = Personne.objects.all()
    return render(request, 'cv.html',{'personne':personne_object})
# Create your views here.



def afficher_cv(request, personne_id):
    # Récupérer la personne en fonction de l'ID
    personne = get_object_or_404(Personne, id=personne_id)

    # Charger les autres données
    formations = Formation.objects.all()
    experiences = Experience.objects.all()
    competences = Competence.objects.all()

    # Passer les données au contexte
    context = {
        "personne": personne,
        "formations": formations,
        "experiences": experiences,
        "competences": competences,
    }
    return render(request, "cv.html", context)

