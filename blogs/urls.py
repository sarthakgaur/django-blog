from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^posts$', views.posts, name='posts'),
    re_path(r'^new_post$', views.new_post, name='new_post'),
    re_path(r'^edit_post/(?P<post_id>\d+)/$', views.edit_post, name='edit_post'),
]