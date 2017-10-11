from django.conf.urls import url
from . import views


app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),  # name的正确性以及结尾的逗号，否则
    # 会报NoReverseMatch at /post/2/Reverse for 'post_comment' with arguments '(2,)' and keyword arguments '{}'
    # not found. 0 pattern(s) tried: []的错误
]