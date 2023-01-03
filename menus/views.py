from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from menus.models import Menu

# Create your views here.
def index(request):
    context = dict()
    menus = Menu.objects.all()
    today = str(datetime.now().date())
    context["today"] = today
    context["menus"] = menus
    return render(request, 'menus/index.html', context=context)


def detail(request, pk):
    menu=Menu.objects.get(id=pk)
    return render(request, 'menus/detail.html', {"menu":menu})