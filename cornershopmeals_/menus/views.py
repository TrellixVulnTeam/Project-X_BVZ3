from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from menus.forms import CreateNewMenu
from menus.models import Menu


# Create your views here.
def create_menu(request):
    if request.method == 'POST':
        menu = CreateNewMenu(request.POST)
        if menu.is_valid():
            menu.save()
        m = Menu.objects.latest('menu_date')
        print('JJlatestM: ', m)
        return show_latest_menu(request=request, menu=m)
    else:
        menu = CreateNewMenu()
    content = {'form': menu}
    return render(request, 'menus/create_menus.html', content)


def show_latest_menu(request, menu=None, menu_id=None):
    if not menu or not menu_id:
        menu = Menu.objects.latest('menu_date')
    return render(request, 'menus/menu.html', context={'menu': menu})


def show_all_menus(request):
    menus = Menu.objects.all()
    print('JJshow_all_menus')
    return render(request, 'menus/all_menus.html', context={'menus': menus})
