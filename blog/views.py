from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from .models import Info, Footer, Newsletter, TechStack, Post
from .forms import NewsletterForm, SearchForm, EmailPostForm
from .feeds import LatestPostsFeed

from taggit.models import Tag


EMAIL = 'django@example.com'


def general_info(request, link_slug):
    """Footer links rendering."""
    query = Footer.objects.filter(link_slug=link_slug)
    title = query.values_list('template_title', flat=True)
    body = query.values_list('template_body', flat=True)
    context = {'title': title[0], 'body': body[0]}
    return render(request, 'blog/general.html', context)


def newsletter(request):
    """Newsletter success page."""
    return render(request, 'blog/newsletter.html')


def homepage(request):
    """Landing page."""
    query = Info.objects.first()
    title = query.home_title
    paragraph = query.home_paragraph
    posts = LatestPostsFeed().items()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            Newsletter.objects.create(email=email)
            return redirect(reverse('blog:newsletter'))
    else:
        form = NewsletterForm()

    context = {
        'title': title,
        'paragraph': paragraph,
        'posts': posts,
        'form': form,
    }
    return render(request, 'blog/home.html', context)


def about_page(request):
    """Informations page for these interested in website."""
    query = Info.objects.first()
    about_blog = query.about_blog
    about_author = query.about_author
    email = query.contact_email
    techstack = TechStack.objects.all()
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
        'about_blog': about_blog,
        'about_author': about_author,
        'techstack': techstack,
        'email': email
    }
    return render(request, 'blog/about.html', context)


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
            return render(request, 'blog/list.html', context)

        else:
            return render(request, 'blog/list.html', {'form': form})

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
        return render(request, 'blog/list.html', context)


def post_detail(request, post):
    """View post."""
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)

    # Similar posts recommendation
    post_topic_list = post.tags.values_list('id', flat=True)
    recommend = Post.published.filter(tags__in=post_topic_list).exclude(id=post.id)
    recommend = recommend.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]

    return render(request, 'blog/detail.html', {'post': post, 'recommend': recommend})


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

            read_post = f'Read post: {post_url}\n\n'
            if not cd['comment']:
                sender_info = f'from: {cd["name"] + " <" + cd["email"] + ">"}'
            else:
                sender_info = f"{cd['name'] + ' <' + cd['email'] + '>'}'s comment:\n{cd['comment']}"
            message = read_post + sender_info
            send_mail(subject, message, EMAIL, [cd['to_mail']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/share.html', {'post': post, 'form': form, 'sent': sent})


def homelab_page(request):
    """Homelab page."""
    return render(request, 'blog/homelab.html')


def reviews_page(request):
    """Reviews page."""
    return render(request, 'blog/reviews.html')


def projects_page(request):
    """Projects page."""
    return render(request, 'blog/projects.html')


def services_page(request):
    """Services page."""
    return render(request, 'blog/services.html')


def metafaq_page(request):
    """Meta+FAQ page."""
    return render(request, 'blog/metafaq.html')
