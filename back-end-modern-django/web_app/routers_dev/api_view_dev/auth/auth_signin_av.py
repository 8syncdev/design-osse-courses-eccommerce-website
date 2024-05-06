from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from web_app.serializers import UserSerializer
from web_app.models import User
from utils.export import ResUtil
from dev_core.security.export import *



class AuthSignInAV(APIView):
    '''
        Sign in API View
            - Purpose: Sign in to authenticate user
            - Request: POST
                - username: string
                - password: string
            - Permission: AllowAny
            - Authentication: None
    '''
    permission_classes = MIX_PERMISSION_ANY
    permission_classes = MIX_PERMISSION_AUTH
    http_method_names=['post']
    name_api = 'Sign In API'


    def post(self, request):
        get_user = User.objects.filter(username=request.data['username']).first()
        if get_user is not None and get_user.check_password(request.data['password']):
            data = {
                    'username': get_user.username,
                    'email': get_user.email,
                    'phone': get_user.phone,
                    'full_name': get_user.full_name,
                    'created_at': get_user.created_at,
                    'updated_at': get_user.updated_at,
                }
            return Response(ResUtil.res_success(
                name_res=AuthSignInAV.name_api,
                data=data
            ), status=status.HTTP_200_OK)
        
        return Response(ResUtil.res_fail(
            name_res=AuthSignInAV.name_api,
            data='Username or password is incorrect!'
        ), status=status.HTTP_401_UNAUTHORIZED)
    

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = self.permission_classes

        return [permission() for permission in self.permission_classes]