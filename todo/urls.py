from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('add-project', views.add_data, name="todo"),
    path('delete_to_do/<int:id>', views.delete_to_do, name="delete_to_do"),
    path('open-to-do/<int:id>', views.open_to_do, name="open_to_do"),
    path('update-to-do/<int:id>', views.update_to_do, name="update_to_do"),
]

