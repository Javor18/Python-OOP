from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTest(TestCase):

    def setUp(self) -> None:
        self.pet_shop = PetShop('Bau')

    def test_correct_init(self):
        self.assertEqual('Bau', self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_with_zero_quantity(self):
        with self.assertRaises(Exception) as err:
            self.pet_shop.add_food('banana', 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(err.exception))

    def test_add_food_that_is_not_available(self):
        self.pet_shop.food = {}

        result = self.pet_shop.add_food('banana', 2)

        self.assertTrue('banana' in self.pet_shop.food)
        self.assertEqual({'banana': 2}, self.pet_shop.food)
        self.assertEqual("Successfully added 2.00 grams of banana.", result)

    def test_add_food_that_is_available(self):
        self.pet_shop.food = {'banana': 2}

        result = self.pet_shop.add_food('banana', 2)

        self.assertTrue('banana' in self.pet_shop.food)
        self.assertEqual({'banana': 4}, self.pet_shop.food)
        self.assertEqual("Successfully added 2.00 grams of banana.", result)

    def test_add_pet_that_is_not_available(self):
        self.pet_shop.pets = []

        result = self.pet_shop.add_pet('dog')

        self.assertTrue('dog' in self.pet_shop.pets)
        self.assertEqual(['dog'], self.pet_shop.pets)
        self.assertEqual("Successfully added dog.", result)

    def test_add_pet_that_is_available(self):
        self.pet_shop.pets = ['dog']

        with self.assertRaises(Exception) as err:
            self.pet_shop.add_pet('dog')

        self.assertEqual("Cannot add a pet with the same name", str(err.exception))

    def test_feed_pet_that_is_not_available(self):
        self.pet_shop.pets = ['cat']

        with self.assertRaises(Exception) as err:
            self.pet_shop.feed_pet('z', 'dog')

        self.assertEqual("Please insert a valid pet name", str(err.exception))

    def test_feed_pet_with_not_available_food(self):
        self.pet_shop.pets = ["cat"]
        self.pet_shop.food = {}

        result = self.pet_shop.feed_pet("meat", "cat")
        self.assertEqual('You do not have meat', result)

    def test_food_under_100_quantity(self):
        self.pet_shop.pets = ['cat']
        self.pet_shop.food = {'meat': 2}

        result = self.pet_shop.feed_pet("meat", "cat")
        self.assertEqual(1002, self.pet_shop.food["meat"])
        self.assertEqual("Adding food...", result)

    def test_feed_pet_decreasing_food(self):
        self.pet_shop.pets = ['cat']
        self.pet_shop.food = {'meat': 1200}

        result = self.pet_shop.feed_pet("meat", "cat")

        self.assertEqual(1100, self.pet_shop.food['meat'])
        self.assertEqual("cat was successfully fed", result)

    def test_repr(self):
        result = repr(self.pet_shop)

        expected_result = f'Shop {self.pet_shop.name}:\n' \
                          f'Pets: {", ".join(self.pet_shop.pets)}'

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()