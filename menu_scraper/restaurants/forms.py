from django import forms

class RestaurantForm(forms.Form):
    name = forms.CharField(label='Restaurant Name', max_length=100)
    location = forms.CharField(label='Location', max_length=100)
    image_url = forms.URLField(label='Image URL')
