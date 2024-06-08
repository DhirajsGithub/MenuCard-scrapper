from django.urls import path
from .views import restaurant_list, restaurant_detail, scrape_restaurant

urlpatterns = [
    path('', restaurant_list, name='restaurant_list'),
    path('restaurant_detail/<int:restaurant_id>/', restaurant_detail, name='restaurant_detail'),
    path('scrape/', scrape_restaurant, name='scrape_restaurant'),
]
