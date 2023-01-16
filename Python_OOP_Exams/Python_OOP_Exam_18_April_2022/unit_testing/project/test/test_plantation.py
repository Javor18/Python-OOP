from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTest(TestCase):

    def setUp(self) -> None:

        self.plantation = Plantation(20)

    def test_init_correct(self):

        self.assertEqual(20, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_error(self):

        with self.assertRaises(Exception) as err:

            self.plantation.size = -5

        self.assertEqual("Size must be positive number!", str(err.exception))

    def test_hire_worker_error(self):

        self.plantation.workers = ['pesho']

        with self.assertRaises(Exception) as err:

            self.plantation.hire_worker('pesho')

        self.assertEqual("Worker already hired!", str(err.exception))

    def test_len_wrong_count(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Martin')
        self.pl.plants['Martin'] = ['Tomatoes']
        self.assertEqual(self.pl.__len__(), 1)

    def test_len_wrong_iterable(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Alexandra')
        self.pl.plants['Alexandra'] = ['plant']
        self.assertEqual(self.pl.__len__(), 1)

    def test_len_not_addition(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Martin')
        self.pl.hire_worker('Alexandra')
        self.pl.plants['Martin'] = ['Tomatoes']
        self.pl.plants['Alexandra'] = ['plant']
        self.assertEqual(self.pl.__len__(), 2)

    def test_planting_worker_not_hired_error(self):

        self.plantation.workers = []

        with self.assertRaises(Exception) as err:

            self.plantation.planting('pesho', 'tomatoes')

        self.assertEqual("Worker with name pesho is not hired!", str(err.exception))

    def test_no_space_for_planting(self):

        self.plantation.size = 1

        self.plantation.hire_worker("Pesho")
        self.plantation.planting("Pesho", "Tomatoes")

        with self.assertRaises(Exception) as err:

            self.plantation.planting("Pesho", "Carrots")

        self.assertEqual("The plantation is full!", str(err.exception))

    def test_planting_correct(self):

        self.plantation.size = 2

        self.plantation.hire_worker("Pesho")
        self.plantation.planting("Pesho", "Tomatoes")

        result = self.plantation.planting("Pesho", "Carrots")

        self.assertEqual("Pesho planted Carrots.", result)

    def test_planting_for_first_time(self):

        self.plantation.size = 2

        self.plantation.hire_worker("Pesho")

        result = self.plantation.planting("Pesho", "Carrots")

        self.assertEqual("Pesho planted it's first Carrots.", result)

    def test_str_wrong_output(self):

        self.assertEqual(Plantation(2).__str__().strip(), 'Plantation size: 2')

        self.plantation1 = Plantation(2)


        self.plantation1.hire_worker('Martin')

        self.plantation1.planting('Martin', 'Radishes')

        self.assertEqual(self.plantation1.__str__().strip(), 'Plantation size: 2\nMartin\nMartin planted: Radishes')

    def test_repr_wrong_output(self):

        self.assertEqual(Plantation(2).__repr__().strip(), 'Size: 2\nWorkers:')

        self.plantation1 = Plantation(2)

        self.plantation1.hire_worker('Martin')

        self.plantation1.planting('Martin', 'Radishes')

        self.assertEqual(self.plantation1.__repr__().strip(), 'Size: 2\nWorkers: Martin')

if __name__ == '__main__':

    main()