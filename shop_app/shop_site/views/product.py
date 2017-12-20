from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from shop_app.models import Product, Tag, Category, Image, Shop, Promotion
from shop_app.shop_site.forms.product import CreateProductForm

def create(request, shopId):
    message = None
    tags = Tag.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            price = request.POST['price']
            category = request.POST['category']
            short_description = request.POST['short_description']
            taxes = request.POST['taxes']
            tag = request.POST['tags']
            model = request.POST['serial']
            description = request.POST['description']
            images = request.FILES['images']
            promotion = request.POST['promotion']
            # published = request.POST['published']

            shop = Shop.objects.get(id=shopId)

            product = Product.objects.create(name=name,
                                             price=price,
                                             category=Category.objects.get(id=category),
                                             shop=shop,
                                             serial=model,
                                             description=description,
                                             short_description=short_description,
                                             published=True,
                                             taxes=taxes)

            # product.tags = Tag.objects.exists(id=tag)
            # product.save()

    #         Capturar las imagenes y crear la entrada en la base de datos...
            images_file = Image.objects.create(src=images, name=name, product=product)
            images_file.save()

            if promotion == True:
                prom = Promotion.objects.create(image=images_file, name=name, product=product)
                prom.save()

    else:
        form = CreateProductForm()
        return render(request, 'product/create.html',
                      {'form': form, 'tags': tags, 'categories': categories, 'shopId': shopId})

    return HttpResponseRedirect(reverse('admin-product-list', args=shopId,))


def index(request, shopId):
    products = Product.objects.filter(shop=shopId)
    return render(request, 'product/list.html', {'products':products, 'shopId':shopId})


