from django.contrib import admin
from .models import CustomUser, Departement, Direction, Filiale
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm 

# Register your models here.

class CustomUserAdmin(UserAdmin): 
    add_form = CustomUserCreationForm 
    model = CustomUser
    list_display = ['email', 'username', 'departements', 'poste', 'is_staff', ]
    add_fieldsets = UserAdmin.add_fieldsets+(
        (None, {'fields' : ('poste',)}),
        (None, {'fields' : ('departements',)}),
        (None, {'fields' : ('directions',)}),
        (None, {'fields' : ('filiales',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Departement)
admin.site.register(Direction)
admin.site.register(Filiale)
