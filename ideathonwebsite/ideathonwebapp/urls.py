from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import  settings
from ideathonwebapp.views import display

urlpatterns = [
    path('',views.home),
    path('register/',views.registerPage),
    path('videos/',display,name='videos'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)