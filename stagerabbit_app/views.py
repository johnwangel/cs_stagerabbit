from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Theater, Production, State, NewProductionForm
from django.conf import settings
from django.conf.urls.static import static
import os
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TheaterSerializer, ProductionSerializer, StateNameSerializer
from operator import and_
from functools import reduce
from django.db.models import Q

class TheaterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows theaters to be viewed or edited
    """
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows productinons to be viewed or edited.
    """
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer
    permission_classes = [permissions.IsAuthenticated]


class StateNameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows productinons to be viewed or edited.
    """
    queryset = State.objects.all()
    serializer_class = StateNameSerializer
    permission_classes = [permissions.IsAuthenticated]  

def my_json():
    return []

def index(request):
    # prod_list=my_json()
    # for theater in prod_list:
    #     for prod in theater['prods']:
    #         p = Production(theater=Theater.objects.all().filter(name=theater['theater_name'])[0],show=prod['title'],start_date=prod['start_date'],end_date=prod['end_date'],venue='Main Stage',description=prod['description'])
    #         p.save()
    states=Theater.objects.order_by('state__name').values('state__name').distinct()
    theaters=Theater.objects.all().values('id','name','city','state__name','state__abbr','state__id')
    context={ 'theaters': theaters, 'states' : states }
    return render(request, 'stagerabbit_app/theaters.html',context)

def productions(request, tid):
    prods=Theater.objects.all().filter(id=tid)
    context={'prods':prods}
    return render(request, 'stagerabbit_app/productions.html',context)

def new_production(request): 
    if request.method == 'POST':
        form = NewProductionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('theaters'))
    else:
        form = NewProductionForm()

    return render(request, 'stagerabbit_app/new_production.html', {'form' : form })

def json(request):
    prod_q=Production.objects.all().filter(show="Steel Magnolias")
    prods=[]
    for prod in prod_q:
        show = { 'theater' : prod.theater.name, 'show': prod.show, 'start': prod.start_date, 'end': prod.end_date, 'venue': prod.venue, 'description' : prod.description  }
        prods.append(show)    
    print (prods)
    return JsonResponse(prods,safe=False)

def search(request):
    term = request.GET.get('search_string','')
    terms = term.split(' ')
    productions = Production.objects.all().filter(reduce(and_, [Q(show__icontains=t) for t in terms])).values('theater__name','theater__city','theater__state__abbr','show','start_date','end_date','description','venue').order_by('start_date')
    return render(request, 'stagerabbit_app/search.html', { 'term': term, 'prods' : productions })