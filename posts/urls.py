from django.urls import path
#from . import views
from .views import HomeView, AddPostView

urlpatterns = [
    #path('postsHome/', views.home, name="home"),
    path('postsHome/', HomeView.as_view(), name="home"),
    path('addPost/', AddPostView.as_view(), name="addPost")
]