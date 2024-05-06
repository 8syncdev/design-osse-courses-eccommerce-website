from rest_framework.serializers import ModelSerializer
from web_app.models import Shoppingcart

class ShoppingcartSerializer(ModelSerializer):
    class Meta:
        model = Shoppingcart
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']