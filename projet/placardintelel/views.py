from django.shortcuts import render
from models import *

# Create your views here.

def home(request):
    historique_receptions = HISTORIQUE_RECEPTIONS.objects.all()
    masse_prelevee = MASSE_PRELEVEE.objects.all()
    masse_actuelle = MASSE_ACTUELLE.objects.all()
    reference_tag = REFERENCE_TAG.objects.all()

    # On fournit les informations a la page 'index.html' (home)
    return render(request,'index.html', {'historique_receptions':historique_receptions, 'masse_prelevee':masse_prelevee, 'masse_actuelle':masse_actuelle, 'reference_tag': reference_tag })
