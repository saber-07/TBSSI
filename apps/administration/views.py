from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import CustomUser, Direction, Departement, Filiale, Application, Mesure, Categorie, Domaine, Referentiel
from .forms import CustomUserCreationForm, EditUserForm
# Create your views here.

class UserCreateView(CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user_list')
    template_name = 'administration/user_new.html'

class UserUpdateView(UpdateView):

    model = CustomUser
    form_class = EditUserForm
    success_url = reverse_lazy('user_list')
    template_name = 'administration/user_edit.html'

class UserDeleteView(DeleteView):
    
    model = CustomUser
    template_name = 'administration/user_delete.html'
    success_url = reverse_lazy('user_list')

class UserListView(ListView):

    model = CustomUser
    template_name = 'administration/user_list.html'

class UserDetailView(DetailView):

    model = CustomUser
    template_name = 'administration/user_detail.html'

class FilialeCreateView(CreateView):

    model = Filiale
    template_name = 'administration/filiale_new.html'
    fields = ['nom_fil']

class FilialeUpdateView(UpdateView):

    model = Filiale
    template_name = 'administration/filiale_edit.html'
    fields = ['nom_fil']

class FilialeDeleteView(DeleteView):
    
    model = Filiale
    template_name = 'administration/filiale_delete.html'
    success_url = reverse_lazy('filiale_list')

class FilialeListView(ListView):

    model = Filiale
    template_name = 'administration/filiale_list.html'

class FilialeDetailView(DetailView):

    model = Filiale
    template_name = 'administration/filiale_detail.html'

class DirectionCreateView(CreateView):

    model = Direction
    template_name = 'administration/direction_new.html'
    fields = ['nom_dir', 'filiales']

class DirectionUpdateView(UpdateView):

    model = Direction
    template_name = 'administration/direction_edit.html'
    fields = ['nom_dir', 'filiales']

class DirectionDeleteView(DeleteView):
    
    model = Direction
    template_name = 'administration/direction_delete.html'
    success_url = reverse_lazy('direction_list')

class DirectionListView(ListView):

    model = Direction
    template_name = 'administration/direction_list.html'

class DirectionDetailView(DetailView):

    model = Direction
    template_name = 'administration/direction_detail.html'

class DepartementCreateView(CreateView):

    model = Departement
    template_name = 'administration/departement_new.html'
    fields = ['nom_dep', 'directions']

class DepartementUpdateView(UpdateView):

    model = Departement
    template_name = 'administration/departement_edit.html'
    fields = ['nom_dep', 'directions']

class DepartementDeleteView(DeleteView):
    
    model = Departement
    template_name = 'administration/departement_delete.html'
    success_url = reverse_lazy('departement_list')

class DepartementListView(ListView):

    model = Departement
    template_name = 'administration/departement_list.html'

class DepartementDetailView(DetailView):

    model = Departement
    template_name = 'administration/departement_detail.html'

class ApplicationCreateView(CreateView):

    model = Application
    template_name = 'administration/application_new.html'
    fields = ['nom_app']

class ApplicationUpdateView(UpdateView):

    model = Application
    template_name = 'administration/application_edit.html'
    fields = ['nom_app']

class ApplicationDeleteView(DeleteView):
    
    model = Application
    template_name = 'administration/application_delete.html'
    success_url = reverse_lazy('application_list')

class ApplicationListView(ListView):

    model = Application
    template_name = 'administration/application_list.html'

class ApplicationDetailView(DetailView):

    model = Application
    template_name = 'administration/application_detail.html'

class ReferentielCreateView(CreateView):

    model = Referentiel
    template_name = 'administration/referentiel_new.html'
    fields = ['nom_referentiel']

class ReferentielUpdateView(UpdateView):

    model = Referentiel
    template_name = 'administration/referentiel_edit.html'
    fields = ['nom_referentiel']

class ReferentielDeleteView(DeleteView):
    
    model = Referentiel
    template_name = 'administration/referentiel_delete.html'
    success_url = reverse_lazy('referentiel_list')

class ReferentielListView(ListView):

    model = Referentiel
    template_name = 'administration/referentiel_list.html'

class ReferentielDetailView(DetailView):

    model = Referentiel
    template_name = 'administration/referentiel_detail.html'

class DomaineCreateView(CreateView):

    model = Domaine
    template_name = 'administration/domaine_new.html'
    fields = ['nom_domaine', 'referentiel']

class DomaineUpdateView(UpdateView):

    model = Domaine
    template_name = 'administration/domaine_edit.html'
    fields = ['nom_domaine', 'referentiel']

class DomaineDeleteView(DeleteView):
    
    model = Domaine
    template_name = 'administration/domaine_delete.html'
    success_url = reverse_lazy('domaine_list')

class DomaineListView(ListView):

    model = Domaine
    template_name = 'administration/domaine_list.html'

class DomaineDetailView(DetailView):

    model = Domaine
    template_name = 'administration/domaine_detail.html'

class CategorieCreateView(CreateView):

    model = Categorie
    template_name = 'administration/categorie_new.html'
    fields = ['nom_categorie', 'domaine']

class CategorieUpdateView(UpdateView):

    model = Categorie
    template_name = 'administration/categorie_edit.html'
    fields = ['nom_categorie', 'domaine']

class CategorieDeleteView(DeleteView):
    
    model = Categorie
    template_name = 'administration/categorie_delete.html'
    success_url = reverse_lazy('categorie_list')

class CategorieListView(ListView):

    model = Categorie
    template_name = 'administration/categorie_list.html'

class CategorieDetailView(DetailView):

    model = Categorie
    template_name = 'administration/categorie_detail.html'

class MesureCreateView(CreateView):

    model = Mesure
    template_name = 'administration/mesure_new.html'
    fields = ['nom_mesure', 'categorie']

class MesureUpdateView(UpdateView):

    model = Mesure
    template_name = 'administration/mesure_edit.html'
    fields = ['nom_mesure', 'categorie']

class MesureDeleteView(DeleteView):
    
    model = Mesure
    template_name = 'administration/mesure_delete.html'
    success_url = reverse_lazy('mesure_list')

class MesureListView(ListView):

    model = Mesure
    template_name = 'administration/mesure_list.html'

class MesureDetailView(DetailView):

    model = Mesure
    template_name = 'administration/mesure_detail.html'