from django import forms

from shop_app.models import Shop
from shop_app.utils.countries import COUNTRIES



class ShopCreateForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Shop name','class':'form-control' })
    )

    address = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Shop address', 'class': 'form-control'})
    )

    latitude = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Latitude', 'class':'form-control'})
    )

    longitude = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Longitude', 'class': 'form-control'})
    )

    phone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder':'Phone', 'class':'form-control'})
    )

    country = forms.ChoiceField(required=True,
                                widget=forms.Select(attrs={'placeholder': 'Country', 'class': 'form-control', 'id': 'country_list'}),
                                choices=COUNTRIES,)


    city = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'})
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder':'Email', 'class':'form-control'})
    )

    #TODO PONERLE EL ICONO A CADA RED SOCIAL EN LA VISTA
    facebook = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'placeholder':'Facebook','class':'form-control'})
    )

    twitter = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'Twitter', 'class': 'form-control'})
    )

    google_plus = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'Google+', 'class': 'form-control'})
    )

    logo = forms.FileField(
        required=False,
        widget=forms.FileInput(attrs={'placeholder':'Logo', 'class':'form-control'})
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder':'Description', 'class':'form-control'})
    )

    class Meta:
        model = Shop
        fields = ('name', 'address', 'latitude', 'longitude', 'phone', 'country', 'city', 'email', 'facebook', 'twitter', 'google_plus', 'logo', 'description', )