from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ItemForm
from .models import Item
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, "index.html", context)


class IndexClassView(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'item_list'


def item(request):
    return HttpResponse("<h1>This is an item view</h1>")


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, "detail.html", context)


class FoodDetail(DetailView):
    model = Item
    template_name = 'detail.html'



def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'item-form.html', {"form": form})


class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)



def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'item-form.html', {"form": form, "item": item})


def delete_item(request, id):
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'item-delete.html', {"item": item})