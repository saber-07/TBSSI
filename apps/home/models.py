from django.db import models
from django.urls import reverse
from apps.administration.models import CustomUser


#les modeles utilisés

#classe Tableau de bord (principale)
class TB(models.Model):
    Intitule = models.CharField(max_length=200, blank=False, unique=True)
    Objectif = models.CharField(max_length=200, blank=False)
    
    def __str__(self):
        return self.Intitule

    def get_absolute_url(self):
        return reverse("tbb_detail", kwargs={"pk": self.pk})
    

    
#classe Indicateur 
class Indicateur(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    PERIODICITE_CHOICES =( ('Annuelle', 'Annuelle'),
                    ('Trimestrielle', 'Trimestrielle'),
                    ('Mensuelle', 'Mensuelle'),
                    )

    TYPE_INDICATEUR_CHOICES = (  
        ('IPP', 'Indicateurs de performance de productivité'),
        ('IPQ', 'Indicateurs de performance de qualité'),
        ('IPC', 'Indicateurs de performance de capacité'),
        ('IPS', 'Indicateurs de performance stratégiques'),
    )

    Intitule_Indicateur = models.CharField(max_length=100, blank=False, unique=True)
    Objectif = models.CharField(max_length=100, default='objectif', blank=False)
    Domaine = models.CharField(max_length=100, default='Sécurité des RH', blank=False)
    Type = models.CharField(max_length=50, default='IPS', choices=TYPE_INDICATEUR_CHOICES, blank=False)
    Methode_calcul = models.CharField(max_length=200, default='Nb utilisateur', blank=False)
    Periodicite = models.CharField(max_length=100, choices=PERIODICITE_CHOICES)
    Source = models.CharField(max_length=100, default='DSSI', blank=False)


    #cle etrangere -> Graphe + TB
    Id_Graphe = models.ForeignKey('Graphe', on_delete=models.CASCADE, blank=False)
    Id_TB = models.ForeignKey(TB, on_delete=models.CASCADE)


    def __str__(self):
        return self.Intitule_Indicateur
    
    def get_absolute_url(self):
        return reverse("indicateur_detail", kwargs={"pk": self.pk})
    

#classe Graphe 
class Graphe(models.Model):
    
    GRAPHES_CHOICES = (
    ('Barres horizontales','Barres horizontales'),
    ('Barres Verticales','Barres Verticales'),
    ('Lineaire','Lineaire'),
    ('Camembert','Camembert'),
    ('Beignet','Beignet')
    ) 

    Type = models.CharField(max_length=50, choices=GRAPHES_CHOICES)

    def __str__(self):
        return self.Type 

#classe donnée
class Donnee(models.Model):

    Date = models.DateField(blank=False)
    Valeur = models.IntegerField(blank=False)
    #cle etrangere indicateur
    Id_Indicateur = models.ForeignKey(Indicateur, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Valeur)

    def get_absolute_url(self):
        return reverse("data_detail", kwargs={"pk": self.pk})
    

#classe interpretation

class Interpretation(models.Model):

    Contenu = models.TextField(blank=False)
    Id_Indicateur = models.ForeignKey(Indicateur, on_delete=models.CASCADE)