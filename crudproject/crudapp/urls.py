from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('show', views.show),
    path('addTask', views.addTask),
    path('updateTask', views.updateTask),
    path('deleteTask', views.deleteTask),
    path('showModalDetails', views.showModalDetails),
 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
