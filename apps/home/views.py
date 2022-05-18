from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from .models import TB,Indicateur,Graphe,Donnee


from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.shortcuts import render 



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    context['ListeTb'] = TB.objects.all()
    context['ListeInd'] = Indicateur.objects.all()
    context['FirstTb'] = TB.objects.all().first()
    context['FirstInd'] = Indicateur.objects.all().first()

    context['ListeDonnees'] = Donnee.objects.all()

    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            context['ListeTb'] = TB.objects.all()
            context['FirstTb'] = TB.objects.all().first()
            context['ListeInd'] = Indicateur.objects.all()
            context['ListeDonnees'] = Donnee.objects.all()
            context['FirstInd'] = Indicateur.objects.all().first()

            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        
        context['ListeTb'] = TB.objects.all()
        context['FirstTb'] = TB.objects.all().first()
        context['ListeInd'] = Indicateur.objects.all()
        context['ListeDonnees'] = Donnee.objects.all()
        context['FirstInd'] = Indicateur.objects.all().first()

        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))



# Create your views here.

class TbDetail(SingleObjectMixin ,ListView):
    template_name = 'home/tbb_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=TB.objects.all())
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tb'] = self.object
        return context

    def get_queryset(self):
        return self.object.indicateur_set.all()
    

class TbCreateView(CreateView):
    model = TB
    template_name = 'home/tbb_new.html'
    fields = ['Intitule', 'Objectif']
    def get_context_data(self,*args, **kwargs):
        context = super(TbCreateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        return context

class TbUpdateView(UpdateView):
    model = TB
    template_name = 'home/tbb_edit.html'
    fields = ['Intitule', 'Objectif']
    def get_context_data(self,*args, **kwargs):
        context = super(TbUpdateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        return context

class TbDeleteView(DeleteView):
    model = TB
    template_name = 'home/tbb_delete.html'
    success_url = reverse_lazy('home')
    def get_context_data(self,*args, **kwargs):
        context = super(TbDeleteView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        return context



class IndicateurCreateView(CreateView):
    model = Indicateur
    template_name = 'home/indicateur_new.html'
    fields = ['Intitule_Indicateur', 'Periodicite', 'Id_Graphe', 'Id_TB'] 


class IndicateurListView(ListView):
    model = Indicateur
    template_name = 'home/indicateur_list.html'

class IndicateurDetailView(DetailView):
    model = Indicateur
    template_name = 'home/indicateur_detail.html'
    def get_context_data(self,*args, **kwargs):
        context = super(IndicateurDetailView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        return context

def listeindicateurview(request):
    return render(request,'home/listeIndicateur.html',
    {'ListeInd' : Indicateur.objects.all(),
    'ListeTb' : TB.objects.all()
})

class IndicateurUpdateView(UpdateView):
    model = Indicateur
    template_name = 'home/indicateur_edit.html'
    fields = ['Intitule_Indicateur', 'Periodicite', 'Id_Graphe', 'Id_TB']

class IndicateurDeleteView(DeleteView):
    model = Indicateur
    template_name = 'home/indicateur_delete.html'
    success_url = reverse_lazy('liste_indicateurs')

class DataCreateView(CreateView):
    model = Donnee
    template_name = 'home/data_new.html'
    fields = ['Date','Valeur','Id_Indicateur']

def listedonneesview(request):
    return render(request,'home/listeDonnees.html',
    {'all_data_list' : Donnee.objects.all(),
    'ListeTb' : TB.objects.all()
})

class DataDetailView(DetailView):
    model = Donnee
    template_name = 'home/data_detail.html'
    def get_context_data(self,*args, **kwargs):
        context = super(DataDetailView, self).get_context_data(*args,**kwargs)
        context['all_data_list'] = Donnee.objects.all()
        return context

class DataDeleteView(DeleteView):
    model = Donnee
    template_name = 'home/data_delete.html'
    success_url = reverse_lazy('liste_donnees')

class DataUpdateView(UpdateView):
    model = Donnee
    template_name = 'home/data_update.html'
    fields = ['Date','Valeur','Id_Indicateur']
