from rest_framework.serializers import ModelSerializer
from web_app.models import Invoice

class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']