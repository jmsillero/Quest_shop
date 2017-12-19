from django.shortcuts import render, redirect

from shop_app.models import Shop, Product
from shop_app.shop_site.forms.shop import ShopCreateForm
from shop_app.utils.countries import COUNTRIES


def index(request):
    user = request.user
    shops = Shop.objects.filter(owner=user)
    return render(request, 'shop/list.html', {'shop_list':shops})

def create(request):
    message = None
    if request.method == 'POST':
        form = ShopCreateForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            address = request.POST['address']
            latitude = request.POST['latitude']
            longitude = request.POST['longitude']

            user = request.user
            owner = user

            phone = request.POST['phone']
            email = request.POST['email']
            facebook = request.POST['facebook']
            twitter = request.POST['twitter']
            google_plus = request.POST['google_plus']
            logo = request.FILES['logo']
            description = request.POST['description']
            country = request.POST['country']
            city = request.POST['city']

            if Shop.objects.filter(email=email):
                message = 'This shop is already in the system'
            else:
                shop = Shop.objects.create(name=name, latitude=latitude, longitude=longitude,
                                           address=address, owner=owner, phone=phone, facebook=facebook,
                                           twitter=twitter, google_plus=google_plus, logo=logo,
                                           description=description, country=country, city=city)
                shop.save()
                return redirect('index')

    else:
        form = ShopCreateForm()

    return render(request, 'shop/create.html', {'form': form, 'message':message})


def show_shop(request, shopId):
    shop = Shop.objects.get(id=shopId)
    country = shop.country
    for c in COUNTRIES:
        if c[0] == country:
            country = c[1]
            break

    shop.country = country

    products_total = Product.objects.filter(shop=shop).count()
    shop.products_count = products_total
    return render(request, 'shop/view.html', {'shop':shop})

