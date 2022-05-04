from django.urls import path 
from .views import member, search, populate, login, create_member, create_member_details, edit, edit_member, edit_member_detail, search_edit
urlpatterns = [
    path('', member, name='member'),
    path('search/', search, name='search'),
    path('populate/', populate, name='populate'),
    path('login/', login, name='login'),
    path('create_member/', create_member, name='create_member'),
    path('create_member_details/', create_member_details, name='create_member_details'),
    path('edit/', edit, name='edit'),
    path('edit_member/<int:id>', edit_member, name='edit_member'),
    path('edit_member_detail/<int:id>', edit_member_detail, name='edit_member_detail'),
    path('search_edit/', search_edit, name='search_edit'),
]
