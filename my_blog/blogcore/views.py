from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.db.models import Count
from .models import Post
from .forms import EmailPostForm, CommentForm

from taggit.models import Tag


def post_list(request, tag_slug=None):
    """Show posts and related data."""
    post_list = Post.published.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blogcore/post/list.html',
                  {'posts': posts, 'tag': tag})


def post_detail(request, post):
    """View post."""
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)
    comments = post.comments.filter(active=True)
    form = CommentForm()

    # Similar posts recommendation
    post_topic_list = post.tags.values_list('id', flat=True)
    recommend = Post.published.filter(tags__in=post_topic_list).\
        exclude(id=post.id)
    recommend = recommend.annotate(same_tags=Count('tags')).\
        order_by('-same_tags', '-publish')[:3]

    return render(request,
                  'blogcore/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'form': form,
                   'recommend': recommend})


def post_share(request, post):
    """Share post via email."""
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = post.title
            message = f"Read post: {post_url}\n\n" +\
                f"{cd['name']}'s comment:\n{cd['comment']}"
            send_mail(subject, message, 'django@example.com', [cd['to_mail']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request,
                  'blogcore/post/share.html',
                  {'post': post, 'form': form, 'sent': sent})


@require_POST
def post_comment(request, post):
    """Post a comment."""
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)
    comment = None

    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request,
                  'blogcore/post/comment.html',
                  {'post': post, 'form': form, 'comment': comment})