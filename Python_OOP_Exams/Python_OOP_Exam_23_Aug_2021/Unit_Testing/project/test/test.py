from project.library import Library
from unittest import TestCase, main


class LibraryTest(TestCase):

    def setUp(self) -> None:

        self.library = Library('iskra')

    def test_correct_init(self):

        self.assertEqual('iskra', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_correct_name(self):

        with self.assertRaises(Exception) as err:
            self.library.name = ''

        self.assertEqual("Name cannot be empty string!", str(err.exception))

    def test_add_book_with_author_not_in_list(self):

        self.library.books_by_authors = {'elisaveta': ['biografia']}

        self.library.add_book('petar', 'puh')
        result = self.library.books_by_authors

        self.assertEqual({'elisaveta': ['biografia'], 'petar': ['puh']}, result)

    def test_add_book_with_title_not_in_list(self):

        self.library.books_by_authors = {'elisaveta': ['biografia']}

        self.library.add_book('elisaveta', 'puh')
        result = self.library.books_by_authors

        self.assertEqual({'elisaveta': ['biografia', 'puh']}, result)

    def test_add_book_with_author_and_title_not_in_list(self):

        self.library.books_by_authors = {}

        self.library.add_book('petar', 'puh')
        result = self.library.books_by_authors

        self.assertEqual({'petar': ['puh']}, result)

    def test_add_reader_with_name_not_in_list(self):

        self.library.readers = {'reader1': []}

        self.library.add_reader('reader2')

        result = self.library.readers

        self.assertEqual({'reader1': [], 'reader2': []}, result)

    def test_reader_in_list(self):

        self.library.readers = {'reader1': []}

        result = self.library.add_reader('reader1')
        expected_result = "reader1 is already registered in the iskra library."

        self.assertEqual(result, expected_result)

    def test_rent_book_with_reader_not_in_list(self):

        self.library.readers = {}

        result = self.library.rent_book('petar', 'elisaveta', 'puh')
        expected_result = "petar is not registered in the iskra Library."

        self.assertEqual(result, expected_result)

    def test_rent_book_with_book_author_not_in_list(self):

        self.library.readers = {'petar': []}
        self.library.books_by_authors = {}

        result = self.library.rent_book('petar', 'elisaveta', 'puh')
        expected_result = "iskra Library does not have any elisaveta's books."

        self.assertEqual(result, expected_result)

    def test_rent_book_with_book_title_not_in_list(self):

        self.library.readers = {'petar': []}
        self.library.books_by_authors = {'elisaveta': []}

        result = self.library.rent_book('petar', 'elisaveta', 'puh')
        expected_result = """iskra Library does not have elisaveta's "puh"."""

        self.assertEqual(result, expected_result)

    def test_rent_book_correct(self):
        self.library.readers = {'petar': []}
        self.library.books_by_authors = {'elisaveta': ['puh']}

        self.library.rent_book('petar', 'elisaveta', 'puh')

        self.assertEqual({'petar': [{'elisaveta': 'puh'}]}, self.library.readers)
        self.assertEqual({'elisaveta': []}, self.library.books_by_authors)


if __name__ == "__main__":

    main()
