from django.contrib import admin
from .models import TB,Donnee,Graphe,Indicateur, Interpretation 

admin.site.register(TB)
admin.site.register(Donnee)
admin.site.register(Graphe)
admin.site.register(Indicateur)
admin.site.register(Interpretation)
