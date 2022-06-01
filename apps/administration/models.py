from django.db import models
from django.contrib.auth.models import AbstractUser, Group

from django.db.models.signals import post_save
from django.dispatch import receiver

#les modeles utilisés

class Filiale(models.Model):

    nom_fil = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.nom_fil

class Direction(models.Model):

    nom_dir = models.CharField(max_length=60, null=True, blank=True)
    filiales = models.ForeignKey(Filiale, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.nom_dir

class Departement(models.Model):

    nom_dep = models.CharField(max_length=60, null=True, blank=True)
    directions = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nom_dep

class CustomUser(AbstractUser):

    POSTE_CHOICES=(
        ('PDG', 'PDG'),
        ('Directeur', 'Directeur'),
        ('Chef département', 'Chef département'),
        ('Ingénieur', 'Ingénieur')
    )

    poste = models.CharField(max_length=50, choices=POSTE_CHOICES, null=True, blank=True)
    departements = models.ForeignKey(Departement, on_delete=models.CASCADE, null=True, blank=True)
    directions = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True, blank=True)
    filiales = models.ForeignKey(Filiale, on_delete=models.CASCADE, null=True, blank=True)
    is_admin = models.BooleanField(default=False)


@receiver(post_save, sender=CustomUser)
def user_post_save(sender, instance, created, *args, **kargs):

    if (instance.is_admin):
        group = Group.objects.get(name='Admin')  
        instance.groups.add(group)

    if(not instance.is_superuser):
        group = Group.objects.get(name=instance.poste) 
        instance.groups.add(group)

post_save.connect(user_post_save, sender=CustomUser)