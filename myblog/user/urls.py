'''
@Description: 
@Author: WuJinBo
@Date: 2019-08-12 20:00:02
@LastEditTime: 2019-08-13 15:07:05
@LastEditors: WuJinBo
'''
# encoding: utf-8
# @Author: TiAmo
# @Project: MyBlogs
# @Time: 2019/8/12 15:14

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),  # 登录
    path('login_form_model/', views.login_for_model,
         name='login_for_model'),  # 登录
    path('register/', views.register, name='register'),  # 注册
    path('logout/', views.logout, name='logout'),  # 登出
    path('user_info/', views.user_info, name='user_info'),  # 登录
    path('change_nickname/', views.change_nickname,
         name='change_nickname'),  # 更改昵称
    path('bind_email/', views.bind_email, name='bind_email'),  # 绑定邮箱
    path('send_verification_code', views.send_verification_code,
         name='send_verification_code'),
    path('change_password/', views.change_password,
         name='change_password'),    # 更改密码
    path('forgot_password/', views.forgot_password,
         name='forgot_password'),  # 忘记密码
]
