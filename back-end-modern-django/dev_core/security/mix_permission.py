from rest_framework.permissions import *
from dev_core.security.custom_permission.user_permission import *
from dev_core.types.export import *


'''
    Custom User Permission
    - Purpose: Check if the user has permission or not in system of django base on the role
'''
# Permission for any user
MIX_PERMISSION_ANY: List[
    Union[AllowAny, CustomAllUserAnyPermission]
] = [AllowAny, CustomAllUserAnyPermission]
# Permission for authenticated user
MIX_PERMISSION_AUTH: List[
    Union[IsAuthenticated, CustomAllUserAuthPermission]
] = [IsAuthenticated, CustomAllUserAuthPermission]
# Permission for admin user
MIX_PERMISSION_ADMIN: List[
    Union[IsAuthenticated, IsAdminUser, CustomAllUserAuthPermission]
] = [IsAuthenticated, IsAdminUser, CustomAllUserAuthPermission]


# All permission
MIX_PERMISSION_ALL_OPTIONS = [
    *MIX_PERMISSION_ANY, 
    *MIX_PERMISSION_AUTH, 
    *MIX_PERMISSION_ADMIN
]