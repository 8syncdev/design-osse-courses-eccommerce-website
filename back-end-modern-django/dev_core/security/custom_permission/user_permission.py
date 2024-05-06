from .base_permission import CustomBasePermission
from rest_framework import permissions
from web_app.models import User, Userrole, Role
from utils.export import *


class CustomAllUserAuthPermission(
    CustomBasePermission,
):
    '''
        Custom User Permission
        - Purpose: Check if the user has permission or not in system of django base on the role
        - Input: request, view
        - Output: True/False
    '''
    only_role = None

    def has_permission(self, request, view):
        '''
            Has Permission
                - Purpose: Check if the user has permission or not
                - Input: request, view
                - Output: True/False
        '''
        # print(get_client_ip(request))
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_staff):
            return True

        if request.user.is_authenticated:
            userrole = Userrole.objects.get(user=request.user)
            role = userrole.role.role_name
            # print(role)
            if role in self.ROLE_VAR:
                return True
        return False

class CustomAllUserAnyPermission(
    CustomBasePermission,
):
    '''
        Custom User Permission
        - Purpose: Check if the user has permission or not in system of django base on the role
        - Input: request, view
        - Output: True/False
    '''
    only_role = None

    def has_permission(self, request, view):
        '''
            Has Permission
                - Purpose: Check if the user has permission or not
                - Input: request, view
                - Output: True/False
        '''
        # print(get_client_ip(request))
        return True