from project.team import Team
from unittest import TestCase, main


class TeamTest(TestCase):

    def setUp(self) -> None:

        self.team = Team("Stars")

    def test_init(self):

        self.assertEqual("Stars", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name(self):

        with self.assertRaises(Exception) as err:

            self.team.name = "Stars1"

        self.assertEqual("Team Name can contain only letters!", str(err.exception))

    def test_add_member(self):

        self.team.members = {'Hristo': 10}

        result = self.team.add_member(**{'Petar': 10, 'George': 15})

        self.assertEqual("Successfully added: Petar, George", result)

    def test_remove_player_that_exist(self):

        self.team.members = {'Petar': 15}

        result = self.team.remove_member('Petar')

        self.assertEqual("Member Petar removed", result)

    def test_remove_player_that_does_not_exist(self):
        self.team.members = {}

        result = self.team.remove_member('Petar')

        self.assertEqual("Member with name Petar does not exist", result)

    def test_gt(self):

        self.team.members = {}

        team1 = Team("TheStars")

        team1.members = {'Hristo': 1}

        result = self.team.__gt__(team1)

        self.assertEqual(False, result)

    def test_len(self):

        self.team.members = {'Ivan': 2, 'Hristo': 3, 'Petar': 4}

        result = self.team.__len__()

        self.assertEqual(3, result)
    #
    # def test_add(self):
    #
    #     team1 = Team("TheStars")
    #
    #     result = self.team.__add__(team1)
    #
    #     self.assertEqual(1, result)

    def test_str(self):

        self.team.members = {'Ivan': 2, 'Hristo': 3, 'Petar': 4}

        expected_result = "Team name: Stars\n"\
                          "Member: Petar - 4-years old\n"\
                          "Member: Hristo - 3-years old\n""" \
                          "Member: Ivan - 2-years old"

        result = self.team.__str__()

        self.assertEqual(expected_result, result)