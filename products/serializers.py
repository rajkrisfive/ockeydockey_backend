from rest_framework import serializers

from products import models as pm


class CategoryModelSerializer(serializers.ModelSerializer):
    """ for Listing"""
    class Meta:
        model = pm.Category
        exclude = ('created', )


class SubCategoryModelSerializer(serializers.ModelSerializer):
    """ for Listing"""
    class Meta:
        model = pm.SubCategory
        exclude = ('created', )


class ProductCreateModelSerializer(serializers.ModelSerializer):
    """ For Creating"""
    class Meta:
        model = pm.Product
        exclude = ()

    def validate(self, attrs):

        if pm.Product.objects.filter(title=attrs['title'], sub_category=attrs['sub_category']): # check for duplicates.
            raise serializers.ValidationError('Product already present')

        return attrs


class ProductListModelSerializer(serializers.ModelSerializer):
    """ For listing purposes"""
    category = serializers.SerializerMethodField()
    sub_category = serializers.SerializerMethodField()

    class Meta:
        model = pm.Product
        exclude = ('created', )

    def get_sub_category(self, obj):
        return obj.sub_category.title

    def get_category(self, obj):
        return obj.sub_category.category.title