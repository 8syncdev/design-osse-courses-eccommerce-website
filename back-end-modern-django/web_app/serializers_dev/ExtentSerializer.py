from rest_framework.serializers import ModelSerializer
from web_app.models import Extent

class ExtentSerializer(ModelSerializer):
    class Meta:
        model = Extent
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']