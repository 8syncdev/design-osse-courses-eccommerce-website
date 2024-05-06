from rest_framework.serializers import ModelSerializer
from web_app.models import Lesson, Course, Detaillesson
from rest_framework import serializers
from .DetaillessonSerializer import DetaillessonSerializer
from django.utils.text import slugify



class LessonSerializer(ModelSerializer):
    #* Add custom fields: to ViewSet can response the data of the related model.
    extent_name = serializers.SerializerMethodField('get_extent_name')


    class Meta:
        model = Lesson
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_extent_name(self, obj):
        get_course = Course.objects.get(lesson=obj)
        return get_course.extent.name
        