from django.urls import path
from . import views

app_name = 'group5'

urlpatterns = [
    path('', views.index, name='index'),
    path('discover/', views.discover, name='discover'),
    path('discover/<int:restaurant_pk>/', views.restaurant_info, name='restaurant_info'),
    path('additem/<int:restaurant_pk>/', views.add_item, name='add_item'),
    path('deleteitem/<int:item_id>/', views.delete_item, name='delete_item'),
    path('mycart/', views.my_cart, name="my_cart"),
    path('contactus/', views.question_create, name="contact_us"),
    path('foodplanner/', views.food_planner, name="food_planner"),
    path('foodplanner/recommendation/', views.recommendation, name="recommendation"),
]
