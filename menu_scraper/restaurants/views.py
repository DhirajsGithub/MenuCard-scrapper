from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, MenuItem
from .forms import RestaurantForm
from .scraper import scrape_menu_images, ocr_image, parse_menu_text

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    form = RestaurantForm()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants, 'form': form})

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant, 'menu_items': menu_items})

def scrape_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant_name = form.cleaned_data['name']
            location = form.cleaned_data['location']
            restaurant_url = form.cleaned_data['image_url']
            
            image_urls = scrape_menu_images(restaurant_url)
            all_menu_items = []
            for image_url in image_urls:
                ocr_text = ocr_image(image_url)
                menu_items = parse_menu_text(ocr_text)
                all_menu_items.extend(menu_items)
            
            restaurant, created = Restaurant.objects.get_or_create(name=restaurant_name, location=location)
            for item_name, price in all_menu_items:
                MenuItem.objects.create(restaurant=restaurant, item_name=item_name, price=price)
            
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurant_list.html', {'form': form})
