from django.urls import path
from . import views

urlpatterns = [
        
    path('signup',views.signup, name='signup'),
    
    # path('api/login',views.my_login, name='login'),
    
        
    #     # CRUD

    # path('api/create-record', views.create_record, name='create-record'),

    # path('api/update-record/<int:pk>', views.update_record, name='update-record'),

    # path('api/record/<int:pk>', views.singular_record, name='record'),

    # path('api/delete-record/<int:pk>', views.delete_record, name='delete-record'),
    
    # path('api/search/', views.search, name='search'),
    
        
    
]