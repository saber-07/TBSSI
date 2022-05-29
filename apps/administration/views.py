from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import CustomUser
from .forms import CustomUserCreationForm, EditUserForm
# Create your views here.

class UserCreateView(CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'administration/user_new.html'

class UserUpdateView(UpdateView):

    model = CustomUser
    form_class = EditUserForm
    success_url = reverse_lazy('home')
    template_name = 'administration/user_edit.html'

class UserDeleteView(DeleteView):
    
    model = CustomUser
    template_name = 'administration/user_delete.html'
    success_url = reverse_lazy('home')