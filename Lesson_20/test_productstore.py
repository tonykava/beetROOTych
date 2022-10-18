from unittest import TestCase
from productstore import ProductStore, Product


class TestProductStore(TestCase):
    def setUp(self):
        self.s = ProductStore()
        self.p = Product('Sport', 'Football T-Shirt', 100)
        self.p2 = Product('Food', 'Ramen', 1.5)

    def test_add(self):
        self.s.add(self.p, 1000)
        self.s.add(self.p2, 100)
        self.assertEqual(round(self.p.price), 130, 'Not equal')
        self.assertEqual(round(self.p2.price, 2), 1.95, 'Not equal')
        self.assertEqual(self.s.products, {self.p: 1000, self.p2: 100})

    def test_set_discount(self):
        self.s.add(self.p2, 100)
        self.s.set_discount('Ramen', 30)
        self.assertEqual(round(self.p2.price, 3), 1.365)

    def test_sell_product(self):
        self.s.add(self.p2, 100)
        self.s.sell_product('Ramen', 50)
        self.assertEqual(self.s.products[self.p2], 50, 'Not equal')
        with self.assertRaises(Exception) as exception_context:
            self.s.sell_product('Ramen', 200)
        self.assertEqual(str(exception_context.exception), 'We dont have so much of this product')

    def test_get_income(self):
        self.s.add(self.p2, 100)
        self.s.sell_product('Ramen', 50)
        self.assertEqual(round(self.s.cash, 1), 97.5, 'Not equal')

    def test_get_all_products(self):
        self.s.add(self.p, 1000)
        self.s.add(self.p2, 100)
        self.assertEqual(self.s.products, {self.p: 1000, self.p2: 100})

    def test_get_product_info(self):
        self.s.add(self.p2, 100)
        self.assertEqual(self.s.get_product_info('Ramen'), (self.p2, 100))

