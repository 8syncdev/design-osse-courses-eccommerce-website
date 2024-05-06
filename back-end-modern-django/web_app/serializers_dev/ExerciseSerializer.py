from rest_framework.serializers import ModelSerializer
from web_app.models import Exercise

class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
