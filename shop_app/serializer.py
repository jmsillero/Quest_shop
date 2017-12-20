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





class ShopSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # products = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ('id',
                  'name',
                  # 'products',
                  'logo',
                  'owner',
                  'latitude',
                  'longitude',
                  'address')



    def get_owner(self, instance):
        return UserSerializer(instance.owner).data

    # def get_products(self, instance):
    #     products = Product.objects.filter(shop=instance)
    #     if products:
    #         products1 = ProductSerializer(products).data
    #     return products1



    def save(self, **kwargs):
        super(Shop, self).save(**kwargs)


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)
    images = serializers.SerializerMethodField()
    shop = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id',
                  'shop',
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

    def get_shop(self, instance):
        return ShopSerializer(instance.shop).data

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


class ProfileSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()
    user = UserSerializer()

    class Meta:
        model = Profile

