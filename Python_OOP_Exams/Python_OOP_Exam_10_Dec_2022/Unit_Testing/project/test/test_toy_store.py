from project.toy_store import ToyStore
from unittest import TestCase, main


class ToyStoreTest(TestCase):

    def setUp(self) -> None:

        self.toy_store = ToyStore()

    def test_init(self):

        expected_result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(expected_result, self.toy_store.toy_shelf)

    def test_add_toy_that_in_the_shelf(self):

        self.toy_store.toy_shelf["A"] = 'tiger'

        with self.assertRaises(Exception) as err:

            self.toy_store.add_toy("A", 'tiger')

        self.assertEqual("Toy is already in shelf!", str(err.exception))

    def test_add_toy_with_not_available_shelf(self):

        with self.assertRaises(Exception) as err:

            self.toy_store.add_toy("H", 'tiger')

        self.assertEqual("Shelf doesn't exist!", str(err.exception))

    def test_add_toy_in_already_taken_shelf(self):

        self.toy_store.toy_shelf["A"] = 'tiger'

        with self.assertRaises(Exception) as err:

            self.toy_store.add_toy("A", 'cat')

        self.assertEqual("Shelf is already taken!", str(err.exception))

    def test_add_toy_correct(self):

        self.toy_store.toy_shelf["A"] = None

        result = self.toy_store.add_toy("A", 'cat')

        self.assertEqual('cat', self.toy_store.toy_shelf["A"])
        self.assertEqual("Toy:cat placed successfully!", result)

    def test_remove_toy_with_not_available_shelf(self):

        with self.assertRaises(Exception) as err:
            self.toy_store.remove_toy("H", 'tiger')

        self.assertEqual("Shelf doesn't exist!", str(err.exception))

    def test_remove_toy_that_is_not_in_the_shelf(self):

        self.toy_store.toy_shelf["A"] = 'tiger'

        with self.assertRaises(Exception) as err:

            self.toy_store.remove_toy("A", 'cat')

        self.assertEqual("Toy in that shelf doesn't exists!", str(err.exception))

    def test_remove_toy_correct(self):
        self.toy_store.toy_shelf["A"] = 'tiger'

        result = self.toy_store.remove_toy("A", 'tiger')

        self.assertEqual(None, self.toy_store.toy_shelf["A"])
        self.assertEqual(f"Remove toy:tiger successfully!", result)


if __name__ == '__main__':

    main()