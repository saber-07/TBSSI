from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

class TbListView(ListView):
    model = Indicateur
    template_name = 'home/indicateur_list.html'
    def get_context_data(self,*args, **kwargs):
        context = super(TbListView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        context['FirstTb'] = TB.objects.all().first()
        context['ListeInd'] = Indicateur.objects.all()
        context['ListeDonnees'] = Donnee.objects.all()
        context['FirstInd'] = Indicateur.objects.all().first()
        return context

class TbDetailView(DetailView):
    model = Indicateur
    template_name = 'home/indicateur_detail.html'
    def get_context_data(self,*args, **kwargs):
        context = super(TbDetailView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        return context

class TbCreateView(CreateView):
    model = TB
    template_name = 'home/indicateur_new.html'
    fields = ['Intitule', 'Objectif']
    def get_context_data(self,*args, **kwargs):
        context = super(TbCreateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        return context

class TbUpdateView(UpdateView):
    model = TB
    template_name = 'home/indicateur_edit.html'
    fields = ['Intitule', 'Objectif']
    def get_context_data(self,*args, **kwargs):
        context = super(TbUpdateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        return context

class TbDeleteView(DeleteView):
    model = TB
    template_name = 'home/indicateur_delete.html'
    success_url = reverse_lazy('indicateur_list')
    def get_context_data(self,*args, **kwargs):
        context = super(TbUpdateView, self).get_context_data(*args,**kwargs)
        context['ListeTb'] = TB.objects.all()
        return context


def ListeIndicateurView(request):
    return render(request,'home/listeIndicateur.html',
    {'ListeInd' : Indicateur.objects.all(),
    'ListeTb' : TB.objects.all()
})


def ListeDonneesView(request):
    return render(request,'home/listeDonnees.html',
    {'ListeDonnees' : Donnee.objects.all(),
    'ListeTb' : TB.objects.all()})
