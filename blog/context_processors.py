from .models import Info, Footer


def title_copyright(request):
    # Retrieve base title
    obj = Info.objects.first()
    return {'base_title': obj.base_title, 'copyright': obj.copyright}


def footer_links(request):
    # Retrieve footer links by membership-section
    footer_links_website = Footer.website.get_queryset()
    footer_links_other = Footer.other.get_queryset()
    footer_links_social = Footer.social.get_queryset()

    return {
        'footer_links_website': footer_links_website,
        'footer_links_other': footer_links_other,
        'footer_links_social': footer_links_social,
    }
