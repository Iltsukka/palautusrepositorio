from statistics2 import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, All, Not, Or
from querybuilder import Querybuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = Querybuilder()
    m1 = query.playsIn('PHI').HasAtLeast(10, 'assists').HasFewerThan(5, 'goals').build()
    

    query = Querybuilder()
    m2 = (query.playsIn("EDM").HasAtLeast(50, "points").build())
    
    query = Querybuilder()
    matcher2 = query.oneOf(m1,m2).build()
    for player in stats.matches(matcher2):
        print(player)

  

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))



if __name__ == "__main__":
    main()
