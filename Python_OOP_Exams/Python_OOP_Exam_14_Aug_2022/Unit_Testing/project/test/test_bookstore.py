from project.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self):
        self.store = Bookstore(10)

    def test_correct__init__(self):
        self.assertEqual(10, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store._Bookstore__total_sold_books)

    def test_correct_total_sold_books(self):
        result = self.store.total_sold_books
        self.assertEqual(0, result)

    def test_correct_book_limit(self):
        result = self.store.books_limit
        self.assertEqual(10, result)

    def test_books_limit_expected_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual('Books limit of 0 is not valid', str(ve.exception))

    def test_correct_book_limit_setter(self):
        self.store.books_limit = 5
        self.assertEqual(5, self.store.books_limit)

    def test_correct__len__(self):
        self.store.availability_in_store_by_book_titles = {'some book': 5, 'another book': 3}
        result = len(self.store)
        self.assertEqual(8, result)

    def test_receive_book_expected_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book('some book', 100)

        self.assertEqual('Books limit is reached. Cannot receive more books!', str(ex.exception))

    def test_receive_book_with_book_not_in_available_books(self):
        result = self.store.receive_book('some book', 5)
        self.assertEqual({'some book': 5}, self.store.availability_in_store_by_book_titles)
        self.assertEqual('5 copies of some book are available in the bookstore.', result)

    def test_receive_book_with_book_already_in_available_books(self):
        self.store.availability_in_store_by_book_titles = {'some book': 5}
        result = self.store.receive_book('some book', 3)
        self.assertEqual(8, self.store.availability_in_store_by_book_titles['some book'])
        self.assertEqual('8 copies of some book are available in the bookstore.', result)

    def test_sell_book_expected_exception_if_book_not_available(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('some book', 5)

        self.assertEqual('Book some book doesn\'t exist!', str(ex.exception))

    def test_sell_book_expected_exception_if_not_enough_copies(self):
        self.store.availability_in_store_by_book_titles = {'some book': 5}

        with self.assertRaises(Exception) as ex:
            self.store.sell_book('some book', 6)

        self.assertEqual('some book has not enough copies to sell. Left: 5', str(ex.exception))

    def test_correct_sell_book(self):
        self.store.availability_in_store_by_book_titles = {'some book': 5}

        result = self.store.sell_book('some book', 4)
        self.assertEqual(1, self.store.availability_in_store_by_book_titles['some book'])
        self.assertEqual(4, self.store._Bookstore__total_sold_books)
        self.assertEqual('Sold 4 copies of some book', result)

        result_2 = self.store.sell_book('some book', 1)
        self.assertEqual(0, self.store.availability_in_store_by_book_titles['some book'])
        self.assertEqual(5, self.store._Bookstore__total_sold_books)
        self.assertEqual('Sold 1 copies of some book', result_2)

    def test_correct__str__with_no_books(self):
        result = str(self.store)
        expected = ['Total sold books: 0', 'Current availability: 0']
        self.assertEqual('\n'.join(expected), result)

    def test_correct__str__with_books(self):
        self.store.availability_in_store_by_book_titles = {'some book': 5, 'another book': 3}
        self.store.sell_book('some book', 2)
        result = str(self.store)
        expected = ['Total sold books: 2', 'Current availability: 6', ' - some book: 3 copies',
                    ' - another book: 3 copies']
        self.assertEqual('\n'.join(expected), result)


if __name__ == "__main__":
    main()