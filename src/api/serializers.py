from rest_framework import serializers

from itemsdb import models as itemsdb_models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = itemsdb_models.Category
        fields = ('slug', 'name')


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = itemsdb_models.Item
        fields = ('id', 'code', 'name', 'active', 'category')
