"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
import datetime

from app.models import Plant1
from .forms import PlantForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    form = PlantForm(request.POST)

    kwargs = {}

    if request.method == 'POST':
        if 'vyber' in request.POST:
            if request.POST['farba']:
                kwargs['farba'] = request.POST['farba']
            if request.POST['typ']:
                kwargs['typ'] = request.POST['typ']
            if request.POST['pouzitie']:
                kwargs['pouzitie'] = request.POST['pouzitie']
            if request.POST['stanovisko']:
                kwargs['stanovisko'] = request.POST['stanovisko']
            if request.POST['slnko']:
                kwargs['slnko'] = request.POST['slnko']
            if request.POST['vlaha']:
                kwargs['vlaha'] = request.POST['vlaha']

            plants = Plant1.objects.filter(**kwargs)

            return render(
                request,
                'app/index.html',
                {
                    'title':'Home Page',
                    'year':datetime.datetime.now().year,
                    'form':form,
                    'plants':plants,
                }
            )

        elif 'tabulka' in request.POST:
            if request.POST['pk']:

                daco = request.POST
                kwak = request.POST.getlist('pk')
                zoznam = Plant1.objects.filter(id__in=request.POST.getlist('pk'))
                months = []

                for i in range(1,13):
                    months.append(datetime.date(2018, i, 1).strftime('%b'))
                return render(
                    request,
                    'app/about.html',
                    {
                        'title':'About',
                        'message':'Your application description page.',
                        'year':datetime.datetime.now().year,
                        'zoznam':zoznam,
                        'range':range(1, 13),
                        'months':months,
                    }
                )
            else:
                return render(
                    request,
                    'app/about.html',
                    {
                        'title':'About',
                        'message':'Your application description page.',
                        'year':datetime.datetime.now().year,
                    }
                )
    else:
        plants = Plant1.objects.all().order_by('rod_lat')
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year':datetime.datetime.now().year,
                'form':form,
                'plants':plants
            }
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Kontakt',
            'message':'Kontaktne udaje:',
            'year':datetime.datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'nazov':'Tabulka kvitnutia',
            'year':datetime.datetime.now().year,
        }
    )

