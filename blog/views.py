from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from .models import Info, Footer, Newsletter, TechStack, Post
from .forms import NewsletterForm, SearchForm, EmailPostForm
from taggit.models import Tag


EMAIL = 'django@example.com'


def homepage(request):
    """Landing page."""
    return render(request, 'blog/home.html')


def general_info(request, link_slug):
    """Footer links rendering."""
    query = Footer.objects.filter(link_slug=link_slug)
    title = query.values_list('template_title', flat=True)
    body = query.values_list('template_body', flat=True)
    context = {'title': title[0], 'body': body[0]}
    return render(request, 'blog/general.html', context)


def about_page(request):
    """Informations page."""
    return render(request, 'blog/about.html')


def post_list(request, tag_slug=None):
    """Unified listing and searching through blog posts."""

    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') + \
                SearchVector('description', weight='B') + \
                SearchVector('body', weight='C')
            search_query = SearchQuery(query)
            results = Post.published.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.3).order_by('-rank')

            paginator = Paginator(results, 5)
            page_number = request.GET.get('page', 1)

            try:
                posts = paginator.page(page_number)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            context = {'form': form, 'query': query, 'results': results, 'posts': posts}
            return render(request, 'blog/post/list.html', context)

        else:
            return render(request, 'blog/post/list.html', {'form': form})

    if 'query' not in request.GET:
        post_list = Post.published.all()

        tag = None
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            post_list = post_list.filter(tags__in=[tag])

        paginator = Paginator(post_list, 5)
        page_number = request.GET.get('page', 1)

        try:
            posts = paginator.page(page_number)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        context = {'form': form, 'query': query, 'posts': posts, 'tag': tag}
        return render(request, 'blog/post/list.html', context)


def post_detail(request, post):
    """View post."""
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)

    # Similar posts recommendation
    post_topic_list = post.tags.values_list('id', flat=True)
    recommend = Post.published.filter(tags__in=post_topic_list).exclude(id=post.id)
    recommend = recommend.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]

    return render(request, 'blog/post/detail.html', {'post': post, 'recommend': recommend})


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
            message = f"Read post: {post_url}\n\n" + f"{cd['name'] + ' <' + cd['email'] + '>'}'s comment:\n{cd['comment']}"
            send_mail(subject, message, EMAIL, [cd['to_mail']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


def homelab_page(request):
    """Homelab page."""
    return render(request, 'blog/homelab.html')


def services_page(request):
    """Services page."""
    return render(request, 'blog/services.html')


def metafaq_page(request):
    """Meta+FAQ page."""
    return render(request, 'blog/metafaq.html')
