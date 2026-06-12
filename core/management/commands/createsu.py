from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        username = "manager"
        password = "admin123456"

        user, created = User.objects.get_or_create(
            username=username
        )

        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    "Superuser created successfully."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    "Superuser password updated."
                )
            )