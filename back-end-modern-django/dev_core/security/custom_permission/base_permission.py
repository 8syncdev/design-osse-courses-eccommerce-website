'''
    Main purpose of this file is to create custom permission for the project.
    Base permission is used to create custom permission for the project.
'''
from web_app.models import User, Userrole, Role
from rest_framework import permissions

class CustomBasePermission(permissions.BasePermission):
    '''
        Custom Base Permission
            - Purpose: Create custom permission for the project
            - Role: admin, manager, student, teacher
            - Dynamic Role: ROLE_VAR when the role is changed in db, the role will be changed in the permission
    '''
    ROLE_VAR = Role.objects.all().values_list('role_name', flat=True)
    EDIT_METHODS = ("PUT", "PATCH")

    #--------------------------------------------------
    
    def has_permission(self, request, view):
        '''
            Has Permission
                - Purpose: Check if the user has permission or not
                - Input: request, view
                - Output: True/False
                - Default: False, deny all permission
        '''
        #* Default: False, deny all permission
        return False
    
    
    def has_object_permission(self, request, view, obj):
        '''
            Has Object Permission
                - Purpose: Limit the permission to the superuser
                - Input: request, view, obj
                - Output: True/False
        '''
        if request.user.is_superuser:
            return True
        
        #* EDIT_METHODS = ("PUT", "PATCH") from CustomUserPermission
        if request.user.is_staff and request.method not in self.EDIT_METHODS:
            return True
        
        #* SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS') from rest_framework.permissions
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #* Default: False, deny all permission if the user is not superuser or staff
        return False
