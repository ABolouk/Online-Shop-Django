from core.management.commands._usercommand import Command as BaseCommand


class Command(BaseCommand):
    help = "Deactivates the user identified by its phone."

    def handle(self, *args, **options):
        super().handle(*args, **options)
        if self.user.is_active:
            self.user.is_active = False
            self.user.save()
            print(self.style.SUCCESS(f"User by phone={self.user.phone}, successfully deactivated."))
