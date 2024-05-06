from django.shortcuts import redirect, HttpResponse
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from dev_core.settings.settings import *
#* Import hasher to hash the password
from django.contrib.auth.hashers import make_password
#* Import slugify to convert the string to slug
from django.utils.text import slugify

class RequireLoginMiddleware:
    """
        Middleware to force users to log in before accessing any page.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        response = self.get_response(request)
        
        return response
    
    def process_view(self, request: HttpRequest, view_func, view_args, view_kwargs):
        # #* Allow the user to access the login page
        # print(request.build_absolute_uri())
        # print(slugify(make_password('21110105anhtudev')))
        if API_ROUTE in request.build_absolute_uri():
            return None
        if request.get_full_path() == '/admin/login/':
            return None
        #* Detect if the user is authenticated
        if not request.user.is_authenticated:
            return redirect('/admin/login/')
        if not request.user.is_active:
            return redirect('/admin/login/')
        if not request.user.is_staff:
            return redirect('/admin/login/')
        if not request.user.is_superuser:
            return redirect('/admin/login/')
        # print(request.get_full_path_info())
        return None