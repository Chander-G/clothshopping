from django.shortcuts import render,redirect
from myapp.models import Cloth
from myapp.forms import ClothAddForm
from django.views.generic import View,CreateView,ListView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy

# Create your views here.
class ClothCreateView(CreateView):
    model=Cloth
    template_name="cloth-add.html"
    form_class = ClothAddForm
    success_url=reverse_lazy("cloth-list")

class ClothListView(ListView):
    model=Cloth
    template_name="cloth-list.html"
    context_object_name='clothees'

class ClothEditView(UpdateView):
    model=Cloth
    form_class=ClothAddForm
    template_name="cloth-edit.html"
    success_url=reverse_lazy("cloth-list")

class ClothDetailView(DetailView):
    model=Cloth
    template_name="cloth-detail.html"
    context_object_name='clothee'

class ClothDeleteView(DeleteView):
    model=Cloth
    template_name="cloth-delete.html"
    success_url=reverse_lazy('cloth-list')
