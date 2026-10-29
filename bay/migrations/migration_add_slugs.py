from django.db import migrations, models
from django.utils.text import slugify


def fill_slugs(apps, schema_editor):
    for model_name in ('OurConcernPageName', 'PartnerPageName'):
        Model = apps.get_model('bay', model_name)
        used = set()
        for obj in Model.objects.all().order_by('id'):
            base = slugify(obj.page_name) or f"page-{obj.pk}"
            slug, i = base, 2
            while slug in used:
                slug = f"{base}-{i}"
                i += 1
            used.add(slug)
            obj.slug = slug
            obj.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('bay', '0012_auto_20261029_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourconcernpagename',
            name='slug',
            field=models.SlugField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='partnerpagename',
            name='slug',
            field=models.SlugField(max_length=120, null=True, blank=True),
        ),
        migrations.RunPython(fill_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='ourconcernpagename',
            name='slug',
            field=models.SlugField(max_length=120, unique=True, blank=True,
                                   help_text="Khali rakhle page name theke auto toiri hobe"),
        ),
        migrations.AlterField(
            model_name='partnerpagename',
            name='slug',
            field=models.SlugField(max_length=120, unique=True, blank=True,
                                   help_text="Khali rakhle page name theke auto toiri hobe"),
        ),
    ]