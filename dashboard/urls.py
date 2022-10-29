from django.urls import path
#from . import views
from .views import HomeView, AddPostView

urlpatterns = [
    #path('postsHome/', views.home, name="home"),
    path('dashHome/updates', HomeView.as_view(), name="update"),
    path('dashHome/', AddPostView.as_view(), name="update")
]