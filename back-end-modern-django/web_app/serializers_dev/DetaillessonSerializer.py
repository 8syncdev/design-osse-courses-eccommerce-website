from rest_framework.serializers import ModelSerializer
from web_app.models import Detaillesson
from rest_framework import serializers


class DetaillessonSerializer(ModelSerializer):
    #* Add custom fields: to ViewSet can response the data of the related model.
    lesson_name = serializers.CharField(source='lesson.name', read_only=True)
    extent_name = serializers.CharField(source='lesson.course.extent.name', read_only=True)


    class Meta:
        model = Detaillesson
        fields = ('id', 'name', 'lesson_name', 'extent_name', 'created_at', 'updated_at', 'content')
        read_only_fields = ['id', 'created_at', 'updated_at']