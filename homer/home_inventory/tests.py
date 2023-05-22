from django.test import TestCase
from .models import Product
import datetime
from decimal import Decimal

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(
            product_name="Gouda Cheese",
            expiry_date=datetime.date(2023, 6, 18),
            product_price=13.99,
            product_quantity=1
        )

        
        # Product.objects.create(
        #     product_name='Wrong Product',
        #     expiry_date=datetime.date(2021, 3, 9),
        #     product_price=-2.38,
        #     product_quantity=-5
        # )

    def test_product_creation(self):
        """Check whether Product model objects are created correctly"""
        gouda = Product.objects.get(product_name="Gouda Cheese")
        # wrong_product = Product.objects.get(product_name="Wrong Product")
        self.assertEqual(gouda.product_name, "Gouda Cheese")
        self.assertEqual(gouda.expiry_date, datetime.date(2023, 6, 18))
        self.assertEqual(gouda.product_price, Decimal(str(13.99)))
        self.assertEqual(gouda.product_quantity, 1)
        # self.assertEqual(wrong_product.product_name, "Wrong Product")
        # self.assertEqual(wrong_product.expiry_date, datetime.date(2021, 3, 9))
        # add other assertions for wrong (negative) values when validators added