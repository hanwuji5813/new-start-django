from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count
# 刚创建了自定义标签文件，需要重启服务器使django可以拾取此文件

register = template.Library()


@register.simple_tag()  # 导入template模块，实例化了一个template.Library类，并将函数装饰为register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]  # 获取数据库中前num篇的文章
"""最新文章模板标签"""


@register.simple_tag()
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')  # 第二参数为精度，第三参数为降序排列
"""归档模板标签"""


@register.simple_tag()
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)  # annotate统计取出post后，
    # 统计每个category id对应多少行记录，filter对结果集过滤，<1表示该分类下没有文章，没有文章的不显示
"""分类模板标签"""


@register.simple_tag()
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)  # annotate统计取出post后，
    # 统计每个category id对应多少行记录，filter对结果集过滤，<1表示该分类下没有文章，没有文章的不显示
"""云模板标签"""