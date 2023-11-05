from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Handbag, Category
from django.views import generic, View
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def gallery(request):
    category = request.GET.get('category')

    if category == None:
        bags = Handbag.objects.all()
    else:
        bags = Handbag.objects.filter(category__name=category)


    categories = Category.objects.all()
    context = {'bags': bags,
    'categories': categories,}
    return render(request, 'photos/gallery.html', context)

@login_required
def addPhoto(request):
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get("image")

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        else:
            category = None

        handbag = Handbag.objects.create(
            category = category,
            description = data['description'],
            image = image,
            price = data['price'],
            bio = data['bio'],
        )

        return redirect('gallery')


    context = {'categories': categories,}
    return render(request, 'photos/add.html', context)

def viewPhoto(request, pk):
    bag = Handbag.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'bag': bag})

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

class HandbagView(View):
    pass
