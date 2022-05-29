from django.db import models
from django.contrib.auth.models import AbstractUser


#les modeles utilisés


class Departement(models.Model):

    nom_dep = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.nom_dep

class Direction(models.Model):

    nom_dir = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.nom_dir

class Filiale(models.Model):

    nom_fil = models.CharField(max_length=60, null=True, blank=True)

    def __Str__(self):
        return self.nom_fil

class CustomUser(AbstractUser):

    POSTE_CHOICES=(
        ('PDG', 'PDG'),
        ('Directeur', 'Directeur'),
        ('Chef département', 'Chef département'),
        ('Ingénieur', 'Ingénieur'),
    )

    poste = models.CharField(max_length=50, choices=POSTE_CHOICES, null=True, blank=True)
    departements = models.ForeignKey(Departement, on_delete=models.CASCADE, null=True, blank=True)
    directions = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True, blank=True)
    filiales = models.ForeignKey(Filiale, on_delete=models.CASCADE, null=True, blank=True)
