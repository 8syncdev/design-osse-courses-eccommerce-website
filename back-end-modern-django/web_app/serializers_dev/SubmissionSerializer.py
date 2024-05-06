from rest_framework.serializers import ModelSerializer
from web_app.models import Submission

class SubmissionSerializer(ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']