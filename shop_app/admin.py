from django.contrib import admin
from shop_app.models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Promotion)
admin.site.register(Shop)

