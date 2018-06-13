"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from app.models import Plant1
from .forms import PlantForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    form = PlantForm(request.POST)

    kwargs = {}

    if request.method == 'POST':
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

        planty = Plant1.objects.filter(**kwargs)

        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
                'form':form,
                'plant':planty,
            }
        )
    else:
        planty = Plant1.objects.none()
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
                'form':form,
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
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

