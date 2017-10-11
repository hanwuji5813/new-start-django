from django.db import models
from django.contrib.auth.models import User  # 用户验证框架
from django.utils.six import python_2_unicode_compatible  # 装饰器，用来兼容python2
from django.urls import reverse
from django.utils.html import strip_tags
import markdown
# Create your models here.


@python_2_unicode_compatible
class Category(models.Model):
    """django要求模型必须继承modles.Modle类"""
    name = models.CharField(max_length=100)  # 分类

    def __str__(self):
        return self.name  # 用来操作数据库时返回str内容便于查看


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)  # 标签

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)
    """正文较长所以使用TextField"""
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    """文章摘要，可有可无，这里使用ChaeField要求必须存入数据，blank=True后就可以允许为空了"""
    excerpt = models.CharField(max_length=200, blank=True)
    """分类与标签，上面已经定义了，这里是把文章对应的数据库表和分类、标签对应的数据库表关联了起来。
    一篇文章只能有一个分类，而一个分类下却可以有多篇文章，这里使用ForeignKey,一对多的关联方式
    一篇文章可以有多个标签，而每个标签下也可有多篇文章，这里使用ManyToManyField，多对多的关联方式
    """
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    """作者，这里的User是从django.contrib.auth.modles导入的，专门用于处理网站注册、登陆等，是写好的模型。
    一个作者科协多篇文章，一篇文章对应一个作者，使用ForeignKey关联"""
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)  # 阅读量，只允许为0或正整数，初始化为0
    # python manage.py makemigration在migrations下创建了一个0001_initial.py的文件告知django我们对模型做什么修改
    # python manage.py migrate检测migrations下的文件，得知修改，将操作译成数据库操作语言，作用于真正的数据库

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-created_time']

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[  # 实例化一个Markdown类，用于渲染body文本
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 将Markdown文本渲染为HTML文本，srtip_tags去掉HTML文本的所有标签，从文本中摘取前54个字符
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        # 调用父类的save方法将数据保存到数据库
        super(Post, self).save(*args, **kwargs)  # 只有新创建的文章才有摘要显示