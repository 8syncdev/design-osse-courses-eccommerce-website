from rest_framework.serializers import ModelSerializer
from web_app.models import Invoicedetails


class InvoicedetailsSerializer(ModelSerializer):
    class Meta:
        model = Invoicedetails
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']