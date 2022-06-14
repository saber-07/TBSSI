from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TB,Indicateur,Donnee, Interpretation
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin as PermissionRequired
from guardian.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
import datetime
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404, render,redirect 

from django.contrib.auth.models import Group

from django.core.mail import send_mail, BadHeaderError
from .forms import RefusForm

from django.urls import resolve

@login_required(login_url="/login/")
def index(request):  # sourcery skip: merge-dict-assign, move-assign-in-block
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    context['ListeTb'] = TB.objects.all()
    context['ListeInd'] = Indicateur.objects.all()
    context['FirstTb'] = TB.objects.all().first()
    context['FirstInd'] = Indicateur.objects.all().first()

    context['ListeDonnees'] = Donnee.objects.all()

    context['currentMonth'] = datetime.date.today().month

    #Ajouter les groupes
    context['DirecteurGroup'] = Group.objects.get(name='Directeur')
    context['AdminGroup'] = Group.objects.get(name='Admin')
    context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
    context['PDGGroup'] = Group.objects.get(name='PDG')
    context['ChefDeptGroup'] = Group.objects.get(name='Chef département')

    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:

#         load_template = request.path.split('/')[-1]

#         if load_template == 'admin':
#             context['ListeTb'] = TB.objects.all()
#             context['FirstTb'] = TB.objects.all().first()
#             context['ListeInd'] = Indicateur.objects.all()
#             context['ListeDonnees'] = Donnee.objects.all()
#             context['FirstInd'] = Indicateur.objects.all().first()

#             return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template

#         html_template = loader.get_template('home/' + load_template)
        
#         context['ListeTb'] = TB.objects.all()
#         context['FirstTb'] = TB.objects.all().first()
#         context['ListeInd'] = Indicateur.objects.all()
#         context['ListeDonnees'] = Donnee.objects.all()
#         context['FirstInd'] = Indicateur.objects.all().first()

#         return HttpResponse(html_template.render(context, request))

#     except template.TemplateDoesNotExist:

#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))

#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))



# Create your views here.

class TbDetail(LoginRequiredMixin,SingleObjectMixin ,ListView):
    login_url = '/login/'
    template_name = 'home/tbb_detail.html'
    permission_required = "home.view_indicateur"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=TB.objects.all())
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tb'] = self.object
        context['ListeTb'] = TB.objects.all()
        context['ListeDonnees'] = Donnee.objects.all()
        context['currentMonth'] = datetime.date.today().month
        context['currentYear'] = datetime.date.today().year

        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        #liste d interpretation
        context['ListeInter'] = Interpretation.objects.all()
        return context

    def get_queryset(self):
        return self.object.indicateur_set.all()
    

class TbCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = TB
    template_name = 'home/tbb_new.html'
    permission_required = "home.create_tb"
    fields = ['Intitule', 'Objectif']
    def get_context_data(self,*args, **kwargs):
        context = super(TbCreateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

class TbUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    login_url = '/login/'
    model = TB
    template_name = 'home/tbb_edit.html'
    permission_required = "home.change_tb"
    fields = ['Intitule', 'Objectif']
    def get_context_data(self,*args, **kwargs):
        context = super(TbUpdateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

class TbDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    login_url = '/login/'
    model = TB
    template_name = 'home/tbb_delete.html'
    permission_required = "home.delete_tb"
    success_url = reverse_lazy('home')
    def get_context_data(self,*args, **kwargs):
        context = super(TbDeleteView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()

         #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        
        return context



class IndicateurCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Indicateur
    fields = ['Intitule_Indicateur', 'Objectif', 'Domaine' , 'Type', 'Methode_calcul' , 'Source' , 'Periodicite','Id_Graphe', 'Id_TB']
    template_name = 'home/indicateur_new.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self,*args, **kwargs):
        context = super(IndicateurCreateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context
    

class IndicateurDetailView(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
    login_url = '/login/'
    model = Indicateur
    template_name = 'home/indicateur_detail.html'
    def get_context_data(self,*args, **kwargs):
        context = super(IndicateurDetailView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()

         #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

@login_required(login_url="/login/")
def listeindicateurview(request):
    return render(request, 'home/listeIndicateur.html', 
    {'ListeInd' : Indicateur.objects.all,
     'ListeTb' : TB.objects.all(),
    'DirecteurGroup' : Group.objects.get(name='Directeur'),
    'AdminGroup' : Group.objects.get(name='Admin'),
    'IngenieurGroup' : Group.objects.get(name='Ingénieur'),
    'PDGGroup' : Group.objects.get(name='PDG'),
    'ChefDeptGroup' : Group.objects.get(name='Chef département')})


class IndicateurUpdateView(LoginRequiredMixin,PermissionRequiredMixin ,UpdateView):
    login_url = '/login/'
    model = Indicateur
    template_name = 'home/indicateur_edit.html'
    permission_required = "home.change_indicateur"
    fields = ['Intitule_Indicateur', 'Periodicite', 'Id_Graphe', 'Id_TB']
    def get_context_data(self,*args, **kwargs):
        context = super(IndicateurUpdateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
         #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

class IndicateurDeleteView(LoginRequiredMixin,PermissionRequiredMixin ,DeleteView):
    login_url = '/login/'
    model = Indicateur
    template_name = 'home/indicateur_delete.html'
    permission_required = "home.delete_indicateur"
    success_url = reverse_lazy('liste_indicateurs')
    def get_context_data(self,*args, **kwargs):
        context = super(IndicateurDeleteView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

class DataCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Donnee
    template_name = 'home/data_new.html'
    fields = ['Date','Valeur']
     
    def form_valid(self, form):
        form.instance.user = self.request.user
        myurl = self.request.get_full_path()
        myurldos = myurl.rsplit('/', 1)[-1]
        print(myurldos)
        form.instance.Id_Indicateur_id = int(myurldos) 
        return super(DataCreateView, self).form_valid(form)

    def get_context_data(self,*args, **kwargs):
        context = super(DataCreateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

@login_required(login_url="/login/")
def listedonneesview(request):
    return render(request,'home/listeDonnees.html',
    {'all_data_list' : Donnee.objects.all(),
    'ListeTb' : TB.objects.all(),
    'DirecteurGroup' : Group.objects.get(name='Directeur'),
    'AdminGroup' : Group.objects.get(name='Admin'),
    'IngenieurGroup' : Group.objects.get(name='Ingénieur'),
    'PDGGroup' : Group.objects.get(name='PDG'),
    'ChefDeptGroup' : Group.objects.get(name='Chef département')
})

class DataDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Donnee
    template_name = 'home/data_detail.html'
    permission_required = "home.view_data"
    def get_context_data(self,*args, **kwargs):
        context = super(DataDetailView, self).get_context_data(*args,**kwargs)
        context['all_data_list'] = Donnee.objects.all()
        context['ListeTb'] = TB.objects.all()
        
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

class DataDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Donnee
    template_name = 'home/data_delete.html'
    permission_required = "home.delete_donnee"
    success_url = reverse_lazy('liste_donnees')
    def get_context_data(self,*args, **kwargs):
        context = super(DataDeleteView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

class DataUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Donnee
    template_name = 'home/data_update.html'
    permission_required = "home.change_donnee"
    fields = ['Date','Valeur','Id_Indicateur']
    def get_context_data(self,*args, **kwargs):
        context = super(DataUpdateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context


#for administration
@login_required(login_url="/login/")
def administrationView(request):
    return render(request,'administration/administration.html',
    {'ListeInd' : Indicateur.objects.all(),
    'ListeTb' : TB.objects.all(),
})

#for interpretation
class InterpretationCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Interpretation
    permission_required = "home.create_interpretation"
    template_name = 'home/interpretation_new.html'
    fields = ['Contenu']

    # pk_url_kwarg = 'interpretation_pk'
    # slug_url_kwarg='Id_indicateur'

    def form_valid(self, form):
        myurl = self.request.get_full_path()
        myurldos = myurl.rsplit('/', 1)[-1]
        print(myurldos)
        
        form.instance.Id_Indicateur_id = int(myurldos) 
        return super(InterpretationCreateView, self).form_valid(form)
    
    def get_context_data(self,*args, **kwargs):
        context = super(InterpretationCreateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context  

    
class InterpretationDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Interpretation
    permission_required = "home.view_interpretation"
    template_name = 'home/interpretation_detail.html'
    def get_context_data(self,*args, **kwargs):
        context = super(InterpretationDetailView, self).get_context_data(*args,**kwargs)
        context['all_data_list'] = Donnee.objects.all()
        context['ListeTb'] = TB.objects.all()
        
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context


class InterpretationUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    model = Interpretation
    permission_required = "home.change_interpretation"
    template_name = 'home/interpretation_edit.html'
    fields = ['Contenu']
    def get_context_data(self,*args, **kwargs):
        context = super(InterpretationUpdateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
         #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context







class ValidationIndicateurDirecteurListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Indicateur
    template_name = 'home/validation_indicateur_directeur.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ValidationIndicateurDirecteurListView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

class ValidationIndicateurDirecteurDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Indicateur
    template_name = 'home/indicateur_detail.html'
    success_url = reverse_lazy('validation_indicateur_directeur')
    
    def get_context_data(self,*args, **kwargs):
        context = super(ValidationIndicateurDirecteurDetailView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

class ValidationIndicateurChefDepListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Indicateur
    template_name = 'home/validation_indicateur_chef_dep.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ValidationIndicateurChefDepListView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context
    
class ValidationIndicateurChefDepDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Indicateur
    template_name = 'home/indicateur_detail.html'
    success_url = reverse_lazy('validation_indicateur_chef_dep')
    
    def get_context_data(self,*args, **kwargs):
        context = super(ValidationIndicateurChefDepDetailView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

@login_required(login_url="/login/")
def valider_ind(request, *args, **kwargs):
    pk = kwargs.get('pk')
    indicateur = get_object_or_404(Indicateur, pk=pk)
    indicateur.validation_directeur = True
    indicateur.save()

    context = {'indicateur': indicateur,
    'all_data_list' : Donnee.objects.all(),
    'ListeTb' : TB.objects.all(),
    'DirecteurGroup' : Group.objects.get(name='Directeur'),
    'AdminGroup' : Group.objects.get(name='Admin'),
    'IngenieurGroup' : Group.objects.get(name='Ingénieur'),
    'PDGGroup' : Group.objects.get(name='PDG'),
    'ChefDeptGroup' : Group.objects.get(name='Chef département')}


    return render(
        request,
        "home/indicateur_detail.html",
        context=context
    )



@login_required(login_url="/login/")
def valider_ind_Bis(request, *args, **kwargs):
    pk = kwargs.get('pk')
    indicateur = get_object_or_404(Indicateur, pk=pk)
    indicateur.validation_chef_dep = True
    indicateur.save()

    context = {'indicateur': indicateur,
    'all_data_list' : Donnee.objects.all(),
    'ListeTb' : TB.objects.all(),
    'DirecteurGroup' : Group.objects.get(name='Directeur'),
    'AdminGroup' : Group.objects.get(name='Admin'),
    'IngenieurGroup' : Group.objects.get(name='Ingénieur'),
    'PDGGroup' : Group.objects.get(name='PDG'),
    'ChefDeptGroup' : Group.objects.get(name='Chef département')}


    return render(
        request,
        "home/indicateur_detail.html",
        context=context
    )




#Valider Interpretation
class ValidationInterpretationDirecteurListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Interpretation
    template_name = 'home/validation_interpretation_directeur.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ValidationInterpretationDirecteurListView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

class ValidationInterpretationDirecteurDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Interpretation
    template_name = 'home/interpretation_detail.html'
    success_url = reverse_lazy('validation_interpretation_directeur')
    
    def get_context_data(self,*args, **kwargs):
        context = super(ValidationInterpretationDirecteurDetailView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context

class ValidationInterpretationChefDepListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Interpretation
    template_name = 'home/validation_interpretation_chef_dep.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ValidationInterpretationChefDepListView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context
    
class ValidationInterpretationChefDepDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Interpretation
    template_name = 'home/interpretation_detail.html'
    success_url = reverse_lazy('validation_interpretation_chef_dep')
    
    def get_context_data(self,*args, **kwargs):
        context = super(ValidationInterpretationChefDepDetailView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        #Ajouter les groupes
        context['DirecteurGroup'] = Group.objects.get(name='Directeur')
        context['AdminGroup'] = Group.objects.get(name='Admin')
        context['IngenieurGroup'] = Group.objects.get(name='Ingénieur')
        context['PDGGroup'] = Group.objects.get(name='PDG')
        context['ChefDeptGroup'] = Group.objects.get(name='Chef département')
        return context



@login_required(login_url="/login/")
def valider_inter(request, *args, **kwargs):
    pk = kwargs.get('pk')
    interpretation = get_object_or_404(Interpretation, pk=pk)
    interpretation.validation_directeur = True
    interpretation.save()

    context = {'interpretation': interpretation,
    'all_data_list' : Donnee.objects.all(),
    'ListeTb' : TB.objects.all(),
    'DirecteurGroup' : Group.objects.get(name='Directeur'),
    'AdminGroup' : Group.objects.get(name='Admin'),
    'IngenieurGroup' : Group.objects.get(name='Ingénieur'),
    'PDGGroup' : Group.objects.get(name='PDG'),
    'ChefDeptGroup' : Group.objects.get(name='Chef département')}


    return render(
        request,
        "home/interpretation_detail.html",
        context=context
    )



@login_required(login_url="/login/")
def valider_inter_Bis(request, *args, **kwargs):
    pk = kwargs.get('pk')
    interpretation = get_object_or_404(Interpretation, pk=pk)
    interpretation.validation_chef_dep = True
    interpretation.save()

    context = {'interpretation': interpretation,
    'all_data_list' : Donnee.objects.all(),
    'ListeTb' : TB.objects.all(),
    'DirecteurGroup' : Group.objects.get(name='Directeur'),
    'AdminGroup' : Group.objects.get(name='Admin'),
    'IngenieurGroup' : Group.objects.get(name='Ingénieur'),
    'PDGGroup' : Group.objects.get(name='PDG'),
    'ChefDeptGroup' : Group.objects.get(name='Chef département')}


    return render(
        request,
        "home/interpretation_detail.html",
        context=context
    )






#valider rapport 
@login_required(login_url="/login/")
def valider_rapport(request, *args, **kwargs):
    pk = kwargs.get('pk')
    tb = get_object_or_404(TB, pk=pk)
    tb.validation_rapport = True
    tb.save()

    context = {'tb': tb,
    'all_data_list' : Donnee.objects.all(),
    'ListeTb' : TB.objects.all(),
    'DirecteurGroup' : Group.objects.get(name='Directeur'),
    'AdminGroup' : Group.objects.get(name='Admin'),
    'IngenieurGroup' : Group.objects.get(name='Ingénieur'),
    'PDGGroup' : Group.objects.get(name='PDG'),
    'ChefDeptGroup' : Group.objects.get(name='Chef département')}


    return render(
        request,
        "home/tbb_detail.html",
        context=context
    )


   
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def custom_error_403(request, exception):
    return render(request, '403.html', status=403)

def custom_error_500(request):
    return render(request, '500.html', status=500)


@login_required(login_url="/login/")
def refus_indicateur(request, **kwargs):
    pk = kwargs.get('pk')
    ind = get_object_or_404(Indicateur, pk=pk)

    if request.method == 'GET':
        form = RefusForm()
    else : 
        form = RefusForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['motif']
            try:
                send_mail('Indicateur Refusé', message, ind.user.directions.directeur.email, [ind.user.email])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('liste_indicateurs')

    return render(request, "home/email-refus.html", {'form': form})


@login_required(login_url="/login/")
def refus_inter(request, **kwargs):
    pk = kwargs.get('pk')
    inter = get_object_or_404(Interpretation, pk=pk)

    if request.method == 'GET':
        form = RefusForm()
    else : 
        form = RefusForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['motif']
            try:
                send_mail('Interpretation Refusée', message, inter.Id_Indicateur.user.directions.directeur.email, [inter.Id_Indicateur.user.email])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('liste_indicateurs')

    return render(request, "home/email-refus.html", {'form': form})