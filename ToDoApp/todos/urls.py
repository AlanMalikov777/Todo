from django.urls import path
from . import views
urlpatterns = [
    path('', views.list_items),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name ='logout'),
    path('insert/', views.insert, name='insert_item'),
    path('delete/<int:todo_id>', views.delete, name='delete_item'),
]