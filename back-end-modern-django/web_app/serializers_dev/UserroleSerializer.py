from rest_framework.serializers import ModelSerializer
from web_app.models import Userrole

class UserroleSerializer(ModelSerializer):
    class Meta:
        model = Userrole
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']