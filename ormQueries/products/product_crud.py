from .models import Product 
from django.db.models import Q, Avg, Max
from django.db.models.functions import Length

class ProductCrud:
    @classmethod
    def get_all_products(cls):
        return Product.objects.all()

    @classmethod
    def find_by_model(cls, model_name):
        return Product.objects.get(model=model_name)
    
    @classmethod
    def last_record(cls):
        return Product.objects.last()

    @classmethod
    def by_rating(cls, selected_rating):
        return Product.objects.filter(rating=selected_rating)

    @classmethod
    def by_rating_range(cls, min_rating, max_rating):
        return Product.objects.filter(rating__range=(min_rating, max_rating))

    @classmethod
    def by_rating_and_color(cls, selected_rating, selected_color):
        return Product.objects.filter(rating=selected_rating, color=selected_color)

    @classmethod
    def by_rating_or_color(cls, selected_rating, selected_color):
        return Product.objects.filter(Q(rating=selected_rating) | Q(color=selected_color))

    @classmethod
    def no_color_count(cls):
        return Product.objects.filter(color=None).count()

    @classmethod
    def below_price_or_above_rating(self, selected_price, selected_rating):
        return Product.objects.filter(price_cents__lt=selected_price) | Product.objects.filter(rating__gt=selected_rating)

    @classmethod
    def ordered_by_category_alphabetical_order_and_then_price_descending(cls):
        return Product.objects.order_by('category','-price_cents')

    @classmethod
    def products_by_manufacturer(cls, selected_manufacturer):
        return Product.objects.filter(manufacturer__icontains=selected_manufacturer)

    @classmethod
    def manufacturer_names_for_query(cls, selected_manufacturer):
        return Product.objects.filter(manufacturer__icontains=selected_manufacturer).values_list('manufacturer', flat=True)

    @classmethod
    def not_in_a_category(cls, selected_category):
        return Product.objects.exclude(category=selected_category)

    @classmethod
    def limited_not_in_a_category(cls, selected_category, limit):
        return Product.objects.exclude(category=selected_category)[:limit]

    @classmethod
    def category_manufacturers(cls, selected_category):
        return Product.objects.filter(category=selected_category).values_list('manufacturer', flat=True)

    @classmethod
    def average_category_rating(cls, selected_category):
        return Product.objects.filter(category=selected_category).aggregate(Avg('rating'))

    @classmethod
    def greatest_price(cls):
        return Product.objects.aggregate(Max('price_cents'))

    @classmethod
    def longest_model_name(cls):
        return Product.objects.order_by(-Length('model')).values_list('id', flat=True)[0]

    @classmethod
    def ordered_by_model_length(cls):
        return Product.objects.order_by(Length('model'))
