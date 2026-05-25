# Generated manually to backfill missing user profiles.

from django.conf import settings
from django.db import migrations


def create_missing_profiles(apps, schema_editor):
    User = apps.get_model('marketplace', 'User')
    UserProfile = apps.get_model('marketplace', 'UserProfile')

    users_without_profiles = User.objects.filter(profile__isnull=True)

    for user in users_without_profiles.iterator(chunk_size=1000):
        UserProfile.objects.create(user=user)


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0004_listing_approval_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(create_missing_profiles, migrations.RunPython.noop),
    ]