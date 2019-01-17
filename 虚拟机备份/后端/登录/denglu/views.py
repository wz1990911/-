from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from denglu.models import UserInfo, UserToken


def md5(user):
    # 导入hashlib
    import hashlib
    # 导入时间
    import time
    # 将时间转坏成字符串类型
    ctime = str(time.time())
    # 对user进行加密
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    # 对加密以后的m进行加盐
    m.update(bytes(ctime, encoding='utf-8'))
    # 返回加密以后的字符串
    return m.hexdigest()


# Create your views here.
class AuthView(APIView):
    def post(self, request, *args, **kwargs):
        ret = {'state_code': 1000, 'msg': None}
        try:
            # 从前段传过来的账号和密码
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            # 去和数据库里面的账号和密码比较 ，如果一致登录成功
            obj = UserInfo.objects.filter(username=user, password=pwd).first()
            if not obj:
                ret['state_code'] = 1001
                ret['msg'] = '用户名或密码错误'

            else:
                # 可以自己写一个函数返回随机字符串
                # 为登录账户创建一个token
                token = md5(user)
                # 得到随机字符串　我就开始去token表里面找　有没有　没有就添加　有就更新
                UserToken.objects.update_or_create(user=obj, defaults={"token": token})
                ret['token'] = token
        except Exception as e:
            ret['state_code'] = 1002
            ret['msg'] = '请求异常'

        return JsonResponse(ret)


# http://127.0.0.1:8000/api/v1/auth/


# 这个数据我要让登录以后的用户才可以看到

ORDER_DICT = {
    1: {
        'name': '娃娃',
        'price': 200,
        'size': 18,
        'gender': '男',
        'from': '王哲'
    },
    2: {
        'name': '娃娃２',
        'price': 280,
        'size': 18,
        'gender': '男',
        'from': '吕东泽'
    }
}
# from

class MyPermission(object):
    message = "你无权访问"
    def has_permission(self,request,view):
        if request.user.user_type != '3':
            return False
        return True


from myutils.auth import MyAuthtication
# from myutils.permission import MyPermission
class OrderView(APIView):
    authentication_classes = [MyAuthtication]
    permission_classes = [MyPermission]
    def get(self, request, *args, **kwargs):
        print(request.user.username)
        # # 先判断　用户有没有登录
        ret = {'state_code': 1000, 'msg': '数据认证成功', 'data': ORDER_DICT}
        # if request.user.user_type != '3':
        #     ret = {'state_code': 1001, 'msg': '暂无权限','data':[]}
        #     return JsonResponse(ret)

        return JsonResponse(ret)















