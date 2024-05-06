from rest_framework.serializers import ModelSerializer
from web_app.models import User
from django.utils.html import escape




class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'full_name', 'phone', 'created_at', 'updated_at', 'password')
        read_only_fields = ['id', 'created_at', 'updated_at']

    #* It prevent all XSS attacks, when detect a XSS attack, it will return a 400 error using escape() function
    # def validate(self, attrs): 
    #     return escape(attrs)



