from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import datetime
from foods.models import Menu

# Create your views here.
def index(request):
    context = dict()
    today = datetime.today().date()
    menus = Menu.objects.all()
    context["menus"] = menus
    context["date"] = today
    return render(request, 'foods/index.html', context=context)


def food_detail(request, pk):
    context = dict()
    menu = Menu.objects.get(id=pk)
    context["menu"] = menu
    return render(request, 'foods/detail.html', context=context)

