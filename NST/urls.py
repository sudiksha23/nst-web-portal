from django.contrib import admin
from django.urls import path,include
from django.conf import settings
#from .views import redirect_view
from django.conf.urls.static import static 
from NST import views
from NST import models
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
  #  path('admin', admin.site.urls),
    path("", views.index, name='home'),
    path("index",views.index, name='index'),
    
] 
