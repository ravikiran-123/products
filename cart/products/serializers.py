from rest_framework.serializers import ModelSerializer
from .models import product_details



class product_serializer(ModelSerializer):
    class Meta:
        model=product_details
        fields=["Name","Cost_per_item","Stock_quantity","Volume"]