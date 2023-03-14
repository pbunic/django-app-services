import markdown
from django import template
from django.utils.safestring import mark_safe
from ..models import Post

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


# Website meta
@register.simple_tag
def total_posts():
    return Post.published.count()
