from rest_framework.serializers import ModelSerializer
from web_app.models import CourseCategory


class CourseCategorySerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

