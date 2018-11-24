from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^login/$', views.user_login, name="user_login"),    #-----自己写的login方法
    url(r'^login/$', auth_views.login, name="user_login"),      #使用django内置的登录方法，不是login.html登录页面
    url(r'^new-login/$', auth_views.login, {"template_name": "account/login.html"}, name="user_login_new"),
    url(r'^logout/$', auth_views.logout, {"template_name": "account/logout.html"}, name='user_logout'),
    url(r'^register/$', views.register, name="user_register"),
    url(r'^password-change/$', auth_views.password_change, {"post_change_redirect":"/account/password-change-done"}, name='password_change'),
    url(r'^password-change-done/$', auth_views.password_change_done, name='password_change_done'),
    url(r'^password-reset/$', auth_views.password_reset, {"post_reset_redirect":"/account/password-reset-done"}, name="password_reset"),
    url(r'^password-reset-done/$', auth_views.password_reset_done, name="password_reset_done"),
    url(r'^password-reset-confirm/$', auth_views.password_reset_confirm, name="password_reset_confirm"),
    url(r'^password-reset-complete/$', auth_views.password_reset_complete, name="password_reset_complete"),
]