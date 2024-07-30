
from django.conf import settings
from rest_framework.request import Request
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import Token

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request: Request):
        """

           overwrite the auth to set values in a cookies and do not pass 'acesss token' through the header
           that is: 
               - if header is not set explicitly, get it from the cookies
         """
        try:
            header = self.get_header(request)
            if header is None:
                raw_token = request.COOKIES.get(settings.AUTH_COOKIE)
                print(request,  raw_token)
            else:
                raw_token = self.get_raw_token(header)
            if raw_token is None:
                return None

            validated_token = self.get_validated_token(raw_token)

            return self.get_user(validated_token), validated_token
        except:
            return None