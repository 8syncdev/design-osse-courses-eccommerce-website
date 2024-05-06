from rest_framework.viewsets import ModelViewSet
from web_app.models import Course
from web_app.serializers import CourseSerializer
from dev_core.security.export import *
from dev_core.settings.settings import *
from rest_framework.response import Response
from utils.export import *




class CourseVS(ModelViewSet):
    '''
        ViewSet for Course model
    '''
    http_method_names: HTTP_METHOD_NAME_TYPE = ['get']
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = MIX_PERMISSION_AUTH
    authentication_classes = MIX_AUTHEN_TSJ
    pagination_class = CustomPagination if table_exists_util('course') and Course.objects.count() > 10 else None #* Check if the table exists and the number of records is greater than 10, because when deploying the project modelviewset runs before the table is created, so it will cause an error, preference link: https://stackoverflow.com/questions/57947800/django-migration-creates-table-after-the-viewset-tries-to-access-it

    # Add this method to get the queryset for the Course model
    ...
    def get_permissions(self):
        '''
            Get permissions for the viewset
        '''
        if self.action == 'list':
            permission_classes = MIX_PERMISSION_ANY
        else:
            permission_classes = self.permission_classes
        return [permission() for permission in permission_classes]



