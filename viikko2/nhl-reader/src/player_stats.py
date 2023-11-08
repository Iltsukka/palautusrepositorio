class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        sorted_top = sorted(self.reader, key=lambda player : player.points, reverse=True)
        players_sorted_by_nationality = []
        
        for player in sorted_top:
            if player.nationality == nationality:
                players_sorted_by_nationality.append(player)


        return players_sorted_by_nationality
        