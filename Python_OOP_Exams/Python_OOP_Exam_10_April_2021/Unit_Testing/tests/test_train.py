from project.train.train import Train
from unittest import TestCase, main


class TrainTest(TestCase):

    def setUp(self) -> None:

        self.train = Train('Fast', 3)

    def test_init(self):

        self.assertEqual("Fast", self.train.name)
        self.assertEqual(3, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_error(self):

        self.train.passengers = ["Petar", "Hristo", "Ivan"]

        with self.assertRaises(Exception) as err:

            self.train.add("Aleks")

        self.assertEqual(self.train.TRAIN_FULL, str(err.exception))

    def test_adding_already_available_passenger(self):

        self.train.passengers = ["Hristo"]

        with self.assertRaises(Exception) as err:

            self.train.add("Hristo")

        self.assertEqual(self.train.PASSENGER_EXISTS.format("Hristo"), str(err.exception))

    def test_adding_player_correct(self):

        self.train.passengers = []

        result = self.train.add("Hristo")

        self.assertEqual(self.train.PASSENGER_ADD.format("Hristo"), result)

    def test_remove_passenger_error(self):

        self.train.passengers = []

        with self.assertRaises(Exception) as err:

            self.train.remove("Hristo")

        self.assertEqual(self.train.PASSENGER_NOT_FOUND.format("Hristo"), str(err.exception))

    def test_remove_passenger_correct(self):

        self.train.passengers = ["Hristo"]

        result = self.train.remove("Hristo")

        self.assertEqual(self.train.PASSENGER_REMOVED.format("Hristo"), result)


if __name__ == '__main__':

    main()