from rest_framework.serializers import ModelSerializer
from web_app.models import ShoppingcartDetails

class ShoppingcartDetailsSerializer(ModelSerializer):
    class Meta:
        model = ShoppingcartDetails
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']