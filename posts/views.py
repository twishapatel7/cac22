from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post

# Create your views here.
#def home(request):
#    return render(request, 'posts/home.html')

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class Home0View(ListView):
    model = Post
    template_name = 'home0.html'

class Home1View(ListView):
    model = Post
    template_name = 'home1.html'

class Home2View(ListView):
    model = Post
    template_name = 'home2.html'

class Home3View(ListView):
    model = Post
    template_name = 'home3.html'

class Home4View(ListView):
    model = Post
    template_name = 'home4.html'

class Home5View(ListView):
    model = Post
    template_name = 'home5.html'

class Home6View(ListView):
    model = Post
    template_name = 'home6.html'

class Home7View(ListView):
    model = Post
    template_name = 'home7.html'

class Home8View(ListView):
    model = Post
    template_name = 'home8.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'addPost.html'
    fields = '__all__'