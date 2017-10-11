from django.conf.urls import url
from . import views  # 当前目录导入


app_name = 'blog'  # 视图函数命名空间，告知django这个urls.py属于blog应用；若未添加，会的到NoMatchReversed的异常
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),  # as_view后缺少括号会报需求一值但会有传入两个参数的错误
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
]
# 此处的正则很混乱