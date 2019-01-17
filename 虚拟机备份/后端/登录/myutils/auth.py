
from rest_framework.exceptions import AuthenticationFailed

from rest_framework.authentication import BaseAuthentication
from denglu.models import UserToken

class MyAuthtication(BaseAuthentication):
    def authenticate(self, request):
        # 取出客户端传过来的token
        token = request._request.GET.get('token')

        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise AuthenticationFailed('认证失败')

        return (token_obj.user, token_obj.token)