from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class PaintFactoryTest(TestCase):

    def setUp(self) -> None:

        self.paint_factory = PaintFactory('oscar', 10)

    def test_correct_init(self):

        self.assertEqual('oscar', self.paint_factory.name)
        self.assertEqual(10, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_add_new_valid_ingredient(self):

        self.paint_factory.ingredients = {}

        self.paint_factory.add_ingredient('white', 3)

        self.assertEqual({'white': 3}, self.paint_factory.ingredients)

    def test_add_already_available_ingredient(self):

        self.paint_factory.ingredients = {'white': 3}

        self.paint_factory.add_ingredient('white', 3)

        self.assertEqual({'white': 6}, self.paint_factory.ingredients)

    def test_no_space_for_adding_ingredients(self):

        self.paint_factory.ingredients = {'white': 10}

        with self.assertRaises(Exception) as err:

            self.paint_factory.add_ingredient('white', 3)

        self.assertEqual("Not enough space in factory", str(err.exception))

    def test_ingredient_not_allowed(self):

        with self.assertRaises(Exception) as err:

            self.paint_factory.add_ingredient('purple', 2)

        self.assertEqual("Ingredient of type purple not allowed in PaintFactory", str(err.exception))

    def test_remove_available_ingredient_correct(self):

        self.paint_factory.ingredients = {'white': 3}

        self.paint_factory.remove_ingredient('white', 3)

        self.assertEqual({'white': 0}, self.paint_factory.ingredients)

    def test_remove_available_ingredient_err(self):

        self.paint_factory.ingredients = {'white': 3}

        with self.assertRaises(Exception) as err:

            self.paint_factory.remove_ingredient('white', 6)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(err.exception))

    def test_remove_unavailable_ingredient(self):

        self.paint_factory.ingredients = {'white': 3}

        with self.assertRaises(KeyError) as err:

            self.paint_factory.remove_ingredient('black', 6)

        self.assertEqual("'No such ingredient in the factory'", str(err.exception))

    def test_repr(self):

        self.paint_factory.ingredients = {'white': 3}

        result = f"Factory name: oscar with capacity 10.\n"\
                 f"white: 3\n"

        self.assertEqual(result, self.paint_factory.__repr__())

    def test_products_returns_ingredients(self):

        self.assertEqual(self.paint_factory.ingredients, self.paint_factory.products)


if __name__ == '__main__':

    main()
