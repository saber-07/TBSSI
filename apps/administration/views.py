from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import CustomUser, Direction, Departement, Filiale
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
    fields = ['nom_dir', 'filiales']

class DepartementUpdateView(UpdateView):

    model = Departement
    template_name = 'administration/departement_edit.html'
    fields = ['nom_dir', 'filiales']

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