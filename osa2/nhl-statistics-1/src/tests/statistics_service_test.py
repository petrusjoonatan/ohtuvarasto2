import unittest

from player import Player
from statistics_service import StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]


class EmptyPlayerReaderStub:
    def get_players(self):
        return []


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_finds_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.points, 90)

    def test_search_accepts_partial_name(self):
        self.assertEqual(self.stats.search("Gret").name, "Gretzky")

    def test_search_returns_none_for_missing_player(self):
        self.assertIsNone(self.stats.search("Missing"))

    def test_team_returns_only_players_of_requested_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"],
        )

    def test_team_returns_empty_list_for_missing_team(self):
        self.assertEqual(self.stats.team("PHI"), [])

    def test_top_returns_requested_number_in_points_order(self):
        players = self.stats.top(3)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"],
        )

    def test_top_zero_returns_empty_list(self):
        self.assertEqual(self.stats.top(0), [])

    def test_top_can_return_all_players(self):
        self.assertEqual(
            [player.name for player in self.stats.top(5)],
            ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"],
        )

    def test_top_larger_than_player_count_returns_all_players(self):
        self.assertEqual(
            [player.name for player in self.stats.top(10)],
            ["Gretzky", "Lemieux", "Yzerman", "Kurri", "Semenko"],
        )

    def test_empty_player_list(self):
        stats = StatisticsService(EmptyPlayerReaderStub())

        self.assertIsNone(stats.search("Kurri"))
        self.assertEqual(stats.team("EDM"), [])
        self.assertEqual(stats.top(3), [])
