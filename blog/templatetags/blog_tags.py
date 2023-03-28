from django import template
from django.template.defaultfilters import stringfilter
from ..models import Post

import markdown as md

register = template.Library()

extensions_config = {
    "codehilite": {
        "linenums": ["inline"],
    },
}


@register.filter()
@stringfilter
def f_markdown(value):
    return md.markdown(
        value, extensions=['fenced_code', 'codehilite', 'tables', 'toc'], extension_configs=extensions_config
    )


# Website meta
@register.simple_tag
def total_posts():
    return Post.published.count()
