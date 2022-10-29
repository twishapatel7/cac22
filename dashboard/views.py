from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Update

# Create your views here.
#def home(request):
#    return render(request, 'posts/home.html')

class HomeView(ListView):
    model = Update
    template_name = 'updates.html'

class AddPostView(CreateView):
    model = Update
    template_name = 'index.html'
    fields = '__all__'