from django.db import models
from django.urls import reverse


#les modeles utilisés

#classe Tableau de bord (principale)
class TB(models.Model):
    Intitule = models.CharField(max_length=200)
    Objectif = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Intitule

    def get_absolute_url(self):
        return reverse("indicateur_list", kwargs={"pk": self.pk})
    

    
#classe Indicateur 
class Indicateur(models.Model):
    Intitule_Indicateur = models.CharField(max_length=100)
    Periodicite = models.CharField(max_length=100) #Choices
    #cle etrangere -> Graphe + TB
    Id_Graphe = models.ForeignKey('Graphe', on_delete=models.CASCADE,)
    Id_TB = models.ForeignKey(TB, on_delete=models.CASCADE,)


    def __str__(self):
        return self.Intitule_Indicateur
    
    def get_absolute_url(self):
        return reverse("indicateur_detail", kwargs={"pk": self.pk})
    

#classe Graphe 
class Graphe(models.Model):
    Nom = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)

    def __str__(self):
        return self.Nom 

#classe donnée
class Donnee(models.Model):
    Date = models.DateField()
    Valeur = models.IntegerField()
    #cle etrangere indicateur
    Id_Indicateur = models.ForeignKey(Indicateur, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Valeur)