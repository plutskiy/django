from django.core.management import BaseCommand

from shopapp.models import Order, Producs


class Command(BaseCommand):
    def handle(self, *args, **options):
        order = Order.objects.first()

        products = Producs.objects.all()

        if not products:
            self.stdout.write("NO PRODUCTS")
            return

        for product in products:
            order.products.add(product)

        order.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully added products{order.products.all()}"
            )
        )