from project.movie import Movie
from unittest import TestCase, main


class MovieTest(TestCase):

    def setUp(self) -> None:

        self.movie = Movie('Tiger', 2015, 10)

    def test_init(self):

        self.assertEqual('Tiger', self.movie.name)
        self.assertEqual(2015, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name(self):

        with self.assertRaises(Exception) as err:

            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(err.exception))

    def test_year(self):

        with self.assertRaises(Exception) as err:

            self.movie.year = 2

        self.assertEqual("Year is not valid!", str(err.exception))

    def test_add_new_actor(self):

        self.movie.actors = []

        self.movie.add_actor('Petar')

        self.assertEqual(['Petar'], self.movie.actors)

    def test_already_added_actor(self):

        self.movie.add_actor("Petar")
        result = self.movie.add_actor("Petar")

        self.assertEqual("Petar is already added in the list of actors!", result)

    def test_gt_1(self):

        film2 = Movie("Spiderman", 2018, 15)

        result = self.movie.__gt__(film2)

        self.assertEqual('"Spiderman" is better than "Tiger"', result)

    def test_gt_2(self):

        film2 = Movie("Spiderman", 2018, 5)

        result = self.movie.__gt__(film2)

        self.assertEqual('"Tiger" is better than "Spiderman"', result)

    def test_repr(self):

        self.movie.add_actor("Petar")
        self.movie.add_actor("Denis")
        self.movie.add_actor("Hristo")

        result = "Name: Tiger\n" \
                 "Year of Release: 2015\n" \
                 "Rating: 10.00\n" \
                 "Cast: Petar, Denis, Hristo"

        self.assertEqual(result, self.movie.__repr__())


if __name__ == '__main__':

    main()