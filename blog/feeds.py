import markdown
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
from .models import Post


class LatestPostsFeed(Feed):
    """RSS feed."""
    title = 'My Blog'
    link = reverse_lazy('blog:post_list')
    description = 'Blog description.'

    def items(self):
        return Post.published.all()[:5]

    def item_titles(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords_html(markdown.markdown(item.description), 100)

    def item_pubdate(self, item):
        return item.publish
