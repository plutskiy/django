from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from shopapp.models import Producs, Order


class ProductInline(admin.TabularInline):
    model = Producs.orders.through


@admin.action(description="Archieve product")
def archieve_product(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archieved=True)


@admin.action(description="Unarchieve product")
def unarchieve_product(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archieved=False)


@admin.register(Producs)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline
    ]
    actions = [
        archieve_product,
        unarchieve_product,
    ]
    list_display = "pk", "name", "description_short", "price", "discount", "archieved"
    list_display_links = "name", "pk"
    ordering = "pk",
    search_fields = "name", "price"
    fieldsets = [
        (None, {
            "fields": ("name", "description"),
        }),
        ("Price", {
            "fields": ("price", "discount"),
        }),
        ("Other options", {
            "fields": ("archieved",),
            "classes": ("collapse",),
            "description": "Archieve products",
        }),
    ]

    def description_short(self, obj: Producs) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."


class OrderInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]
    list_display = "delivery_adress", "promocode", "created_at", "user_verbose"
    list_display_links = "delivery_adress",

    def get_queryset(self, request):
        return Order.objects.select_related("user_id")

    def user_verbose(self, obj: Order):
        return obj.user_id.first_name or obj.user_id.username
