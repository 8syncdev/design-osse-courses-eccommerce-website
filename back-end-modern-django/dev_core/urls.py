"""
URL configuration for dev_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from dev_core.settings.settings import *
# print(API_ROUTE)
#--------------------------------------------------------------
# brand_name = 'Group 6: Building website for saling online courses and managing courses'
brand_name = '8 Sync Dev'
admin.site.site_header = brand_name
admin.site.site_title = brand_name
admin.site.index_title = brand_name
#--------------------------- Error 404 ---------------------------
handler404 = 'dev_core.security.provider.handle_404.error_404_view'
#--------------------------------------------------------------
urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
#--------------------------------------------------------------
# Admin
urlpatterns += [
    path('admin/', admin.site.urls, name='admin_login'),
]
#--------------------------------------------------------------
# Url social login
from web_app.social_login.google_api import GoogleLogin

urlpatterns += [
    path(f'{API_ROUTE}/dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path(f'{API_ROUTE}/dj-rest-auth/', include('dj_rest_auth.urls')),
    path(f'{API_ROUTE}/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  
]
#--------------------------------------------------------------
# API View
from web_app.routers import (
    AuthSignInAV, 
    AuthSignUpAV, 
    AuthTokenAV
)

urlpatterns += [
    path(f'{API_ROUTE}/api-view/sign-up/', AuthSignUpAV.as_view(), name='auth_login'),
    path(f'{API_ROUTE}/api-view/sign-in/', AuthSignInAV.as_view(), name='auth_signup'),
    path(f'{API_ROUTE}/api-view/token/', AuthTokenAV.as_view(), name='auth_token'),
]

#--------------------------------------------------------------
# Register View Sets
from web_app.routers import router
urlpatterns += router.urls

#--------------------------------------------------------------
# JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns += [
    path(f'{API_ROUTE}/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(f'{API_ROUTE}/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


