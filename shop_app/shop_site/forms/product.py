from django import forms
from shop_app.models import Category, Tag


class CreateProductForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Product Name', 'class': 'form-control'})

    )

    price = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Price', 'class': 'form-control'})
    )

    # category = forms.ChoiceField(choices=Category.objects.all(),
    #                                      required=True,
    #                                      widget=forms.Select(
    #                                          attrs={'class': 'form-control'}
    #                                      ))
    #
    # tags = forms.MultipleChoiceField(choices=Tag.objects.all(),
    #                                  required=True,
    #                                  widget=forms.CheckboxSelectMultiple(
    #                                      attrs={'class': 'form-control'}
    #                                  ))

    serial = forms.CharField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Model', 'class': 'form-control'}))

    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'placeholder': 'Description', 'class': 'form-control'}))

    short_description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'placeholder':'Short Description', 'class': 'form-control'})
    )

    taxes = forms.DecimalField(
        required=True,
        widget=forms.NumberInput(attrs={'placeholder': 'Taxes', 'class': 'form-control'})
    )

    images = forms.ImageField(required=False,
                              widget=forms.FileInput(attrs={'placeholder':'Images',   'multiple':'true'}))

    promotion = forms.BooleanField(required=True,
                                   widget=forms.RadioSelect(attrs={'placeholder':'Is Promotion', 'class': 'form-control'}))
