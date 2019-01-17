from django import forms
from captcha.fields import CaptchaField

# 所有表单类都要继承自 forms.Form
class UserForm(forms.Form):
    # label参数用于设置<label>标签
    # max_length限制字段输入的最大长度。它同时起到两个作用：
    # 一是在浏览器页面限制用户输入不可超过字符数，
    # 二是在后端服务器验证用户输入的长度也不可超过。
    username = forms.CharField(label='用户名', max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    # widget=forms.PasswordInput用于指定该字段在form表单里表现为<input type='password' />，也就是密码输入框。
    password = forms.CharField(label='密码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')