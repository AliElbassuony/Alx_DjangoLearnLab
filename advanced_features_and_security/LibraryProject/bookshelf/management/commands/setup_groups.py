from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Set up user groups and permissions for Book model'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Book)

        perms = {
            "can_view": Permission.objects.get(codename="can_view", content_type=content_type),
            "can_create": Permission.objects.get(codename="can_create", content_type=content_type),
            "can_edit": Permission.objects.get(codename="can_edit", content_type=content_type),
            "can_delete": Permission.objects.get(codename="can_delete", content_type=content_type),
        }

        groups = {
            "Viewers": [perms["can_view"]],
            "Editors": [perms["can_view"], perms["can_create"], perms["can_edit"]],
            "Admins": list(perms.values())
        }

        for group_name, permissions in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.set(permissions)
            group.save()
            self.stdout.write(self.style.SUCCESS(f"{'Created' if created else 'Updated'} group: {group_name}"))
