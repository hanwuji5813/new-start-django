from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)  # 获取被评论的文章

    if request.method == 'POST':  # (注意大小写)
        form = CommentForm(request.POST)

        if form.is_valid():  # 检验表单的数据是否合格
            comment = form.save(commit=False)  # 不保存到数据库
            comment.post = post  # 将评论与被评论的文章关联
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()  # 获取post对应的全部评论，类似于Post.objects.filter()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)