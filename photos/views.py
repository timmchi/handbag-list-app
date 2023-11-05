from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Handbag, Category
from django.views import generic, View
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy


# Create your views here.

class HandbagListView(generic.ListView):
    model = Handbag

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category == None:
            return self.model.objects.all()
        else:
            return self.model.objects.filter(category__name=category)

    def get_context_data(self, **kwargs):
        context = super(HandbagListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class HandbagCreate(LoginRequiredMixin, CreateView):
    model = Handbag
    fields = '__all__'
    success_url = reverse_lazy('gallery')

    def get_context_data(self, **kwargs):
        context = super(HandbagCreate, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class HandbagDetailView(DetailView):
    model = Handbag
