from rest_framework.serializers import ModelSerializer
from web_app.models import Discount

class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']