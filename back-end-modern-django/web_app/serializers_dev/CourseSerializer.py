from rest_framework.serializers import ModelSerializer
from web_app.models import Course, Lesson
from rest_framework import serializers
from .LessonSerializer import LessonSerializer
from rest_framework.response import Response
# import slugify
from django.utils.text import slugify



class CourseSerializer(ModelSerializer):
    #* Add custom fields: to ViewSet can response the data of the related model.
    instructor_name = serializers.CharField(source='instructor.full_name', read_only=True)
    discount_percent = serializers.FloatField(source='discount.discount_percentage', read_only=True)
    extent_name = serializers.CharField(source='extent.name', read_only=True)
    slug = serializers.SerializerMethodField('get_slug')

    #* -----------------------------
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'price','instructor_name', 'discount_percent', 'extent_name', 'created_at', 'updated_at', 'slug')
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_slug(self, obj):
        return slugify(obj.title)
 