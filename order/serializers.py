from dataclasses import fields
from rest_framework import serializers
from core.models import Tag, Delivery_orders

class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class  DeliveryOrdersSerializers(serializers.ModelSerializer):
    """serializers for orders objects"""
    
    class Meta:
        model=Delivery_orders
        fields=('Item_name','Order_id','Delivery_addres','Order_date_time')
        read_only_fields = ('id',)
