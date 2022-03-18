from argparse import ArgumentParser

from django.core.management import BaseCommand, CommandError

from core.models import User


class Command(BaseCommand):

    def add_arguments(self, parser: ArgumentParser):
        parser.add_argument("-p", "--phone", required=True, help="Enter a valid phone number.")

    def handle(self, *args, **options):
        phone = options["phone"]
        try:
            self.user = User.objects.get(phone=phone)
        except:
            raise CommandError(f"User by phone={phone} isn't available!")
