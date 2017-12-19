from rest_framework import serializers

from shop_app.models import Category, Product, Tag, Image, Promotion, Shop, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id', 'password', 'is_superuser', 'is_staff', 'user_permissions', 'groups', 'date_joined')




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'name',
                  'image')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id',
                  'name')


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'src', 'name')


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'price',
                  'tags',
                  'category',
                  'images',
                  'serial',
                  'description',
                  'created_at')

    def get_category(self, instance):
        return CategorySerializer(instance.category).data

    def get_images(self, instance):
        images = Image.objects.filter(product=instance)
        if images:
            images = ImagesSerializer(images, many=True).data
        return images


class PromotionSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    class Meta:
        model = Promotion
        fields = ('id',
                  'name',
                  'product',
                  'image')

    def get_product(self, instance):
        return ProductSerializer(instance.product).data

    def get_image(self, instance):
        return ImagesSerializer(instance.image).data



class ShopSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    owner = serializers.ReadOnlyField(source='owner.username')
    products = ProductSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = Shop
        fields = ('id',
                  'name',
                  'products',
                  'images',
                  'categories',
                  'owner',
                  'latitude',
                  'longitude',
                  'address')

    def get_images(self, instance):
        return ImagesSerializer(instance.images).data

    def get_owner(self, instance):
        return UserSerializer(instance.owner).data

    def get_products(self, instance):
        products = Product.objects.filter(shop=instance)
        if products:
            products = ProductSerializer(products).data
        return products

    def get_categories(self, instance):
        categories = Category.objects.filter(product=instance.product)
        if categories:
            categories = CategorySerializer(categories).data
        return categories;

    def save(self, **kwargs):
        super(Shop, self).save(**kwargs)



class ProfileSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()
    user = UserSerializer()

    class Meta:
        model = Profile

