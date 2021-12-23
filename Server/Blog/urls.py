from django.urls import path
from django.conf import settings
from .views import About, Config, CreatePost, Detais, Home, LoginRegister, Profile, Search
from django.conf.urls.static import static

urlpatterns = [
    path('', Home,name='home_page'),
    
    path('search/', Search),
    
    path('details/<int:id_post>/', Detais),
    
    path('profile/<str:user_name>/', Profile),
    path('profile/<str:user_name>/create/', CreatePost),
    path('profile/<str:user_name>/config/', Config),
    
    path('auth/<path:path>/', LoginRegister),
    
    path('about/', About),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)