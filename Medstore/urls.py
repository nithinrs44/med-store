from django import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('mainapp.urls')),
    
    path('api/', include('mainappapi.urls')),
]
    


