from django.contrib.auth.models import User
from django.core.management import BaseCommand

from shopapp.models import Order


class Command(BaseCommand):
    '''
    Creates orders
    '''
    def handle(self, *args, **options):
        self.stdout.write("Create orders")
        user = User.objects.get(username="plut")
        order = Order.objects.get_or_create(
            delivery_adress = "ул.Пожарского д.20",
            promocode="LETO23",
            user_id=user
        )
        self.stdout.write(self.style.SUCCESS(f"Created order {order}"))