from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        username = "manager"
        password = "admin123"

        if not User.objects.filter(username=username).exists():

            User.objects.create_superuser(
                username=username,
                password=password
            )

            self.stdout.write(
                self.style.SUCCESS(
                    "Superuser created successfully."
                )
            )

        else:

            self.stdout.write(
                self.style.WARNING(
                    "Superuser already exists."
                )
            )