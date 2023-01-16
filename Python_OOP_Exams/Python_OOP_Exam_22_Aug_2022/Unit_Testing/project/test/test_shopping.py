from project.shopping_cart import ShoppingCart

from unittest import TestCase, main


class ShoppingCartTest(TestCase):

    def setUp(self) -> None:

        self.shopping_cart = ShoppingCart('Oscar', 1000)

    def test_correct_init(self):

        self.assertEqual('Oscar', self.shopping_cart.shop_name)
        self.assertEqual(1000, self.shopping_cart.budget)
        self.assertEqual({}, self.shopping_cart.products)

    def test_shop_name_property(self):

        with self.assertRaises(Exception) as err:

            self.shopping_cart.shop_name = 'oscar1'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(err.exception))

    def test_add_product_to_cart_error(self):

        with self.assertRaises(Exception) as err:

            self.shopping_cart.add_to_cart('pizza', 123.5)

        self.assertEqual("Product pizza cost too much!", str(err.exception))

    def test_add_product_to_cart_correct(self):

        self.shopping_cart.products = {}
        result = self.shopping_cart.add_to_cart('pizza', 20)

        self.assertEqual(result, "pizza product was successfully added to the cart!")
        self.assertEqual({'pizza': 20}, self.shopping_cart.products)

    def test_remove_product_from_cart_error(self):

        self.shopping_cart.products = {}

        with self.assertRaises(Exception) as err:
            self.shopping_cart.remove_from_cart('pizza')

        self.assertEqual("No product with name pizza in the cart!", str(err.exception))

    def test_remove_product_from_cart_correct(self):

        self.shopping_cart.products = {'pizza': 20}

        self.shopping_cart.remove_from_cart('pizza')

        self.assertEqual({}, self.shopping_cart.products)

    def test_create_new_shop_instance(self):

        first = ShoppingCart('Test', 200)
        first.add_to_cart('from_first', 1)

        second = ShoppingCart('SecondTest', 100)
        second.add_to_cart('from_second', 2)

        merged = first.__add__(second)
        self.assertEqual('TestSecondTest', merged.shop_name)
        self.assertEqual(300, merged.budget)
        self.assertEqual({'from_first': 1, 'from_second': 2}, merged.products)

    def test_buy_product_error(self):

        self.shopping_cart.products = {'pizza': 30, 'donut': 20, 'meat': 1000}

        with self.assertRaises(Exception) as err:

            self.shopping_cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 50.00lv!", str(err.exception))

    def test_buy_product_correct(self):
        self.shopping_cart.products = {'pizza': 30, 'donut': 20}

        result = self.shopping_cart.buy_products()

        self.assertEqual('Products were successfully bought! Total cost: 50.00lv.', result)


if __name__ == '__main__':

    main()
