from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
)
from .models import Post
from .forms import EmailPostForm, CommentForm, SearchForm
from taggit.models import Tag


def homepage(request, tag_slug=None):
    """Landing page."""
    return render(request, 'blog/home.html')


def about_page(request, tag_slug=None):
    """Informations page."""
    return render(request, 'blog/about.html')


def soc_page(request, tag_slug=None):
    """SOC page."""
    return render(request, 'blog/soc.html')


def post_list(request, tag_slug=None):
    """Unified searching through blog posts."""

    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            results = Post.published.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.3).order_by('-rank')

            paginator = Paginator(results, 9)
            page_number = request.GET.get('page', 1)

            try:
                posts = paginator.page(page_number)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            return render(
            request, 'blog/post/list.html', {'form': form, 'query': query, 'results': results, 'posts': posts}
            )

        else:
            return render(request, 'blog/post/list.html', {'form': form})

    if 'query' not in request.GET:
        post_list = Post.published.all()

        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            post_list = post_list.filter(tags__in=[tag])

        paginator = Paginator(post_list, 9)
        page_number = request.GET.get('page', 1)

        try:
            posts = paginator.page(page_number)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render(
            request, 'blog/post/list.html', {'form': form, 'query': query, 'posts': posts, 'tag': tag}
        )


def post_detail(request, post):
    """View post."""
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)
    comments = post.comments.filter(active=True)
    form = CommentForm()

    # Similar posts recommendation
    post_topic_list = post.tags.values_list('id', flat=True)
    recommend = Post.published.filter(tags__in=post_topic_list).exclude(id=post.id)
    recommend = recommend.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]

    return render(request,
                  'blog/post/detail.html',
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
            message = f"Read post: {post_url}\n\n" + f"{cd['name']}'s comment:\n{cd['comment']}"
            send_mail(subject, message, 'django@example.com', [cd['to_mail']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


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
    return render(request, 'blog/post/comment.html', {'post': post, 'form': form, 'comment': comment})


def services_page(request, tag_slug=None):
    """Services page."""
    return render(request, 'blog/services.html')
