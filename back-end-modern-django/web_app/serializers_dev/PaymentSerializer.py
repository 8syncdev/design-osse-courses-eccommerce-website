from rest_framework.serializers import ModelSerializer
from web_app.models import Payment

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        