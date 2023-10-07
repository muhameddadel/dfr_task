from django.urls import path
from .views import *


app_name = 'category'


urlpatterns = [
    path('', list_categories, name='list-categories'),
    path('create/', create_category, name='create-category'),
    path('<int:pk>/', retrieve_category, name='retrieve-category'),
    path('<int:pk>/update/', update_category, name='update-category'),
    path('<int:pk>/delete/', delete_category, name='delete-category'),
]