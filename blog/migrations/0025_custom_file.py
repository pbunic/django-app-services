from django.db import migrations


def populate_defaults(apps, schema_editor):
    Info = apps.get_model('blog', 'Info')
    defaults = {
        'base_title': 'Title',
        'home_title': 'Title',
        'home_paragraph': 'Paragraph',
        'about_blog': 'blog',
        'about_author': 'author',
        'contact_email': 'mail@example.com',
        'copyright': '(c)',
    }

    # Check if there are any existing instances
    if not Info.objects.exists():
        # If no instances exist, create a new one with default values
        new_instance = Info(**defaults)
        new_instance.save()


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0024_alter_info_about_author_alter_info_about_blog_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_defaults),
    ]
