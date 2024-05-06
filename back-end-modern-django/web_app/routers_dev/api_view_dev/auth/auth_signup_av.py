from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from web_app.serializers import UserSerializer
from web_app.models import User, Userrole
from utils.export import ResUtil
from dev_core.security.export import *
from rest_framework.exceptions import APIException



class AuthSignUpAV(APIView):
    '''
        Sign up API View
            - Purpose: Sign up to create user
            - Request: POST
                - username: string
                - email: string
                - password: string
            - Permission: AllowAny
    '''
    permission_classes = MIX_PERMISSION_AUTH
    authentication_classes = MIX_AUTHEN_TSJ
    http_method_names=['post']
    name_api = 'Sign Up API'


    def post(self, request):
        serializer = UserSerializer(data=request.data)
        try:
            if serializer.is_valid():
                print('serializer.valid')
                user: User = serializer.save()
                user.set_password(request.data['password'])
                user.save()
                data = {
                    'username': user.username,
                    'email': user.email,
                    'full_name': user.full_name,
                    'phone': user.phone,
                    'created_at': user.created_at,
                    'updated_at': user.updated_at,
                }
                # #* Create user role
                get_role = Role.objects.filter(role_name='student').first()
                if not get_role:
                    get_role = Role.objects.create(role_name='student')
                    get_role.save()
                userrole = Userrole.objects.create(user=user, role=get_role)
                userrole.save()
                return Response(ResUtil.res_success(
                    name_res=AuthSignUpAV.name_api,
                    data=data
                ), status=status.HTTP_200_OK)
        except Exception as e:
            return Response(ResUtil.res_fail(
                name_res=AuthSignUpAV.name_api,
                data={
                    'status': 400,
                    'message': 'Username or email is exist! Exception!',
                    'error': f'{serializer.errors}, Exception: {e}'
                }
            ), status=status.HTTP_400_BAD_REQUEST)
        return Response(ResUtil.res_fail(
                name_res=AuthSignUpAV.name_api,
                data={
                    'status': 400,
                    'message': 'Username or email is exist! Error!',
                    'error': f'{serializer.errors}'
                }
            ), status=status.HTTP_400_BAD_REQUEST)
    
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = MIX_PERMISSION_ANY
        else:
            self.permission_classes = self.permission_classes
        return [permission() for permission in self.permission_classes]