from rest_framework.serializers import ModelSerializer
from web_app.models import Role

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']