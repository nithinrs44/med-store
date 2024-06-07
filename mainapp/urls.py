from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.homepg, name=''),
    
    path('register',views.register, name='register'),
    
    path('login',views.my_login, name='login'),
    
    path('logout',views.logout, name='logout'),
    
    path('dashboard',views.dashboard, name='dashboard'),
    
        # CRUD

    path('dashboard', views.dashboard, name='dashboard'),

    path('create-record', views.create_record, name='create-record'),

    path('update-record/<int:pk>', views.update_record, name='update-record'),

    path('record/<int:pk>', views.singular_record, name='record'),

    path('delete-record/<int:pk>', views.delete_record, name='delete-record'),
    
    path('search/', views.search, name='search'),
    
        
    
]