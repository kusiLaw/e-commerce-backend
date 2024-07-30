from django.conf import settings
from rest_framework_simplejwt.views import(
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)


"""
  These custom view overwrite the default dehaviour by setting response data
  in a httponly secure cookies to prevent data from being read by malicious code. Though the reponse is return as default
"""

class CustomTokenObtainPairView(TokenObtainPairView):
    '''
        set secure httponly cookies  in response data
    '''
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            response.set_cookie(
                'access', 
                access_token,
                max_age=settings.AUTH_COOKIES_ACCESS_MAX_AGE,
                path=settings.AUTH_COOKIES_PATH,
                secure=settings.AUTH_COOKIES_SECURE,
                httponly=settings.AUTH_COOKIES_HTTP_ONLY,
                samesite=settings.AUTH_COOKIES_SAMESITE
            )

            response.set_cookie(
                'refresh', 
                refresh_token,
                max_age=settings.AUTH_COOKIES_REFRESH_MAX_AGE,
                path=settings.AUTH_COOKIES_PATH,
                secure=settings.AUTH_COOKIES_SECURE,
                httponly=settings.AUTH_COOKIES_HTTP_ONLY,
                samesite=settings.AUTH_COOKIES_SAMESITE
            )
        return response


class CustomTokenRefreshView(TokenRefreshView):
    """
       - obtain refresh token from cookies and set to request data
       - set new access token in secure cookies
    """
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')

        if refresh_token:
            request.data['refresh'] = refresh_token

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token=response.data.get('access')

            response.set_cookie(
                'access', 
                access_token,
                max_age=settings.AUTH_COOKIES_ACCESS_MAX_AGE,
                path=settings.AUTH_COOKIES_PATH,
                secure=settings.AUTH_COOKIES_SECURE,
                httponly=settings.AUTH_COOKIES_HTTP_ONLY,
                samesite=settings.AUTH_COOKIES_SAMESITE
            )

        return response


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        access_token = request.COOKIES.get('access')

        if access_token:
            request.data['token'] = access_token
        
        return super().post(request, *args, **kwargs)
