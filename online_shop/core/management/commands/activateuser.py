from core.management.commands._usercommand import Command as BaseCommand


class Command(BaseCommand):
    help = "Activates the user identified by its phone."

    def handle(self, *args, **options):
        super().handle(*args, **options)
        if not self.user.is_active:
            self.user.is_active = True
            self.user.save()
            print(self.style.SUCCESS(f"User by phone={self.user.phone}, successfully activated."))
