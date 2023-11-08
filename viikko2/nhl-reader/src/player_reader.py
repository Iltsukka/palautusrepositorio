import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        
    def get_players(self):
        response_dict = requests.get(self.url).json()
        players = []

        for player_dict in response_dict:
            player = Player(player_dict)
            players.append(player)

        return players
