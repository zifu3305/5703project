from rest_framework.authentication import TokenAuthentication, BaseAuthentication, get_authorization_header
from rest_framework import exceptions
import jwt
from django.contrib.auth import get_user_model
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError
from datetime import datetime, timedelta
from django.utils import timezone
# 获取全局的user模型
MTUser = get_user_model()


def generate_jwt(user):
    """
    对user对象的id和时间戳进行jwt加密，作为认证信息
    """
    # expire_time = datetime.now() + timedelta(days=7) 没有时区信息
    expire_time = timezone.now() + timedelta(days=7)  # 有时区信息
    return jwt.encode({'userid': user.pk, 'exp': expire_time}, key=settings.SECRET_KEY).decode('utf-8')


class JWTAuthentication(BaseAuthentication):
    """
    用户认证类
    """
    keyword = 'jwt'  # jwt为token的认证关键字，进行合法性校验

    def authenticate(self, request):
        """
        用户校验方法
        """
        auth = get_authorization_header(request).split()  # 读取request下的header指定authorization字段信息，存储用户认证信息

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None
        # jwt格式校验
        if len(auth) == 1:
            msg = "不可用的JWT请求头"
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = '不可用的JWT请求头！JWT Token中间不应该有空格！'
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]
            jwt_info = jwt.decode(jwt_token, settings.SECRET_KEY)  # jwt解密，获取userid
            userid = jwt_info.get('userid')
            try:
                user = MTUser.objects.get(pk=userid)
                return user, jwt_token
            except:
                msg = "用户不存在"
                raise exceptions.AuthenticationFailed(msg)
        except ExpiredSignatureError:
            msg = "JWT Token过期"
            raise exceptions.AuthenticationFailed(msg)