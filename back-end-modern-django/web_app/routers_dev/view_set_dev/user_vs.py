from rest_framework.viewsets import ModelViewSet
from web_app.models import User
from web_app.serializers import UserSerializer
from dev_core.security.export import *
from dev_core.export import *
from utils.export import *
from rest_framework.decorators import action
from rest_framework.response import Response


class UserVS(ModelViewSet):
    '''
        User View Set
            - Purpose: CRUD User
            - Permission: IsAuthenticated, IsAdminUser
            - Authentication: JWT, Token, Session
    '''
    http_method_names: HTTP_METHOD_NAME_TYPE = ['get']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = MIX_PERMISSION_ADMIN
    authentication_classes = MIX_AUTHEN_TSJ
    pagination_class = CustomPagination if table_exists_util('user') and User.objects.count() > 10 else None

    @action(methods=['get'], detail=False,url_path='get-user-by-token')
    def get_user_by_token(self, request): #* Dont pk => not pass: main_route/pk/custom_route
        '''
            Get User By Token
                - Purpose: Get user by token
                - Request: GET
                    - token: string
                - Permission: IsAuthenticated, IsAdminUser
                - Authentication: JWT, Token, Session
        '''
        print(request.user.is_authenticated)
        if request.user.is_authenticated == False:
            return Response(ResUtil.res_fail(
                name_res='Get User By Token',
                data='Token not found'
            ))
        
        return Response(ResUtil.res_success(
            name_res='Get User By Token',
            data={
                'username': request.user.username,
                'email': request.user.email,
                'phone': request.user.phone,
                'last_login': request.user.last_login,
            }
        ))
        # get_user_from_email = User.objects.filter(token=request.GET.get('token')).first()
        # if get_user_from_email:
        #     return Response(ResUtil.res_success(
        #         name_res='Get User By Token',
        #         data=UserSerializer(get_user_from_email).data
        #     ))
        # return Response(ResUtil.res_fail(
        #     name_res='Get User By Token',
        #     data='Token not found'
        # ))
    
    def get_permissions(self):
        if self.action == 'get_user_by_token':
            self.permission_classes = MIX_PERMISSION_AUTH
        return [permission() for permission in self.permission_classes]


            
    
    

