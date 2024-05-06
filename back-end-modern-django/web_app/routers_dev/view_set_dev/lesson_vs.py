from rest_framework.viewsets import ModelViewSet
from web_app.models import Lesson, Course
from web_app.serializers import LessonSerializer
from dev_core.security.export import *
from dev_core.settings.settings import *
from rest_framework.decorators import action
from rest_framework.response import Response
from utils.export import *


class LessonVS(ModelViewSet):
    '''
        ViewSet for Course model
    '''
    http_method_names: HTTP_METHOD_NAME_TYPE = ['get']
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = MIX_PERMISSION_AUTH
    authentication_classes = MIX_AUTHEN_TSJ
    pagination_class = CustomPagination if table_exists_util('lesson') and Lesson.objects.count() > 10 else None

    # Add this method to get the queryset for the Course model
    ...
    
    #* =>*/lessons/pk/list_lesson_of_course/
    @action(detail=True, methods=['get'], url_path='list-lesson-of-course')
    def list_lesson_of_course(self, request, pk=None):
        '''
            Get all lessons of a course
        '''
        paginator = self.pagination_class()
        try:
            course = Course.objects.get(pk=pk)
            lessons = Lesson.objects.filter(course=course).order_by('id') #* Fixxed error UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'web_app.models_dev.Lesson.Lesson'> QuerySet, using order_by('id') to fix it.

            page = paginator.paginate_queryset(lessons, request)
            serializer = LessonSerializer(page, many=True)
            data = paginator.get_paginated_response(serializer.data).data
            return Response({
                'links': data['links'],
                'count': data['count'],
                'results': [ 
                    {
                        'id': lesson['id'],
                        'name': lesson['title'],
                        'extent_name': lesson['extent_name'],
                        'updated_at': lesson['updated_at'],
                    } for lesson in data['results']
                ]
            })
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        
    def get_permissions(self):
        '''
            Get the permission for the viewset
        '''
        #* Deny the permission for the list action if the user is not an admin
        if self.action == 'list_lesson_of_course': # * Name of the action function
            permission_classes = MIX_PERMISSION_ANY
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]
