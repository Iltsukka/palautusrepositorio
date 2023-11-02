import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_search_working_as_intended(self):
        pelaaja = self.stats.search('Kurri')
        self.assertAlmostEqual(str(pelaaja), 'Kurri EDM 37 + 53 = 90')
    
    def test_searching_for_nonexistent_player(self):
        pelaaja = self.stats.search('Kalapuikko')
        self.assertIsNone(pelaaja)
    
    def test_filtering_players_of_same_team(self):
        pelaajat = self.stats.team('EDM')
        merkkijonona = ([str(item) for item in pelaajat])
        self.assertAlmostEqual(merkkijonona, ['Semenko EDM 4 + 12 = 16', 'Kurri EDM 37 + 53 = 90', 'Gretzky EDM 35 + 89 = 124'])

    def test_top_returns_sorted_list(self):
        pelaajat = self.stats.top(1)
        listassa = [str(pelaaja) for pelaaja in pelaajat]
        print(listassa)
        self.assertAlmostEqual(listassa, ['Gretzky EDM 35 + 89 = 124', 'Lemieux PIT 45 + 54 = 99'])
