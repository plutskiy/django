from django.core.management import BaseCommand

from shopapp.models import Producs


class Command(BaseCommand):
    """
    Creates products
    """
    def handle(self, *args, **options):
        self.stdout.write("Create products")
        products_names =[
            'TV',
            'iPhone',
            'MacBook',
            'Dyson',
            'Microwawe'
        ]
        for product_name in products_names:
            product, created = Producs.objects.get_or_create(name=product_name)
            self.stdout.write(f"Created product {product.name}")
        self.stdout.write(self.style.SUCCESS("Producs succesfully created!"))