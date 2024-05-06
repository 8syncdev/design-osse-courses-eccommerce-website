from rest_framework.viewsets import ModelViewSet
from web_app.models import Detaillesson, Lesson
from web_app.serializers import DetaillessonSerializer
from dev_core.security.export import *
from dev_core.export import *
from utils.export import *
from rest_framework.decorators import action
from rest_framework.response import Response
#* Slugify is used to convert a string to a slug
from django.utils.text import slugify




class DetailLessonVS(ModelViewSet):
    #^ ViewSet for Detaillesson model
    '''
        DetailLesson View Set
            - Purpose: CRUD Detaillesson
            - Permission: IsAuthenticated
            - Authentication: JWT, Token, Session
    '''
    http_method_names: HTTP_METHOD_NAME_TYPE = ['get']
    queryset = Detaillesson.objects.all()
    serializer_class = DetaillessonSerializer
    permission_classes = MIX_PERMISSION_AUTH
    authentication_classes = MIX_AUTHEN_TSJ
    pagination_class = CustomPagination if table_exists_util('detaillesson') and Detaillesson.objects.count() > 10 else None

    # Add this method to get the queryset for the Course model
    ...

    @action(detail=True, methods=['get'], url_path='list-detaillesson-of-lesson')
    def list_detaillesson_of_lesson(self, request, pk=None):
        '''
            Get all detaillessons of a lesson
        '''
        paginator = self.pagination_class()
        try:
            lesson = Lesson.objects.get(pk=pk)
            detaillessons = Detaillesson.objects.filter(lesson=lesson).order_by('id') #* Fixxed error UnorderedObjectListWarning: Pagination may yield inconsistent results with an unordered object_list: <class 'web_app.models_dev.Lesson.Lesson'> QuerySet, using order_by('id') to fix it.

            page = paginator.paginate_queryset(detaillessons, request)
            serializer = DetaillessonSerializer(page, many=True)
            data = paginator.get_paginated_response(serializer.data).data
            return Response({
                'links': data['links'],
                'count': data['count'],
                'results': [ 
                    {
                        'id': detaillesson['id'],
                        'name': detaillesson['name'],
                        'extent_name': detaillesson['extent_name'],
                        'updated_at': detaillesson['updated_at'],
                        'slug': slugify(detaillesson['name']) #* Convert the name to a slug
                    } for detaillesson in data['results']
                ]
            })
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    def get_permissions(self):
        '''
            Get the permission for the viewset
        '''
        #* Deny the permission for the list action if the user is not an admin
        if self.action == 'list':
            permission_classes = MIX_PERMISSION_ADMIN
        elif self.action == 'retrieve' or self.action == 'list_detaillesson_of_lesson':
            permission_classes = MIX_PERMISSION_ANY
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]
    



