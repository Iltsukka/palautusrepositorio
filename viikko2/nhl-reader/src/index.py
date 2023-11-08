from player_reader import PlayerReader
from player_stats import PlayerStats

def main(nationality):
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url).get_players()
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)


    print("Players from " + nationality + ':\n')    
    for player in players:
            print(player)
    print('\n')

if __name__ == "__main__":
    main('FIN')

