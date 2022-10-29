from django.urls import path
#from . import views
from .views import HomeView, Home0View, Home1View, Home2View, Home3View, Home4View, Home5View, Home6View, Home7View, Home8View, AddPostView

urlpatterns = [
    #path('postsHome/', views.home, name="home"),
    path('postsHome8/', Home8View.as_view(),name="home"),
    path('postsHome7/', Home7View.as_view(),name="home"),
    path('postsHome6/', Home6View.as_view(),name="home"),
    path('postsHome5/', Home5View.as_view(),name="home"),
    path('postsHome4/', Home4View.as_view(),name="home"),
    path('postsHome3/', Home3View.as_view(),name="home"),
    path('postsHome2/', Home2View.as_view(),name="home"),
    path('postsHome1/', Home1View.as_view(),name="home"),
    path('postsHome0/', Home0View.as_view(),name="home"),
    path('postsHome/', HomeView.as_view(), name="home"),
    path('addPost/', AddPostView.as_view(), name="addPost")
]