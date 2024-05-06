from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from dev_core.types.export import *




'''
    TSJ: Token, Session, JWT
    Token có đúng format không, có dính mã độc hại không
    Session có đúng format không, có dính mã độc hại không
    JWT kiểm tra token có đúng không, có dính mã độc hại không
'''
MIX_AUTHEN_TSJ: List[
    Union[BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication]
] = [BasicAuthentication, TokenAuthentication, SessionAuthentication, JWTAuthentication]

