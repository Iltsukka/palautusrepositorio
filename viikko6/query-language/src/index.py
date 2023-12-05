from statistics2 import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, All, Not, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher3 = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )
    matcher2 = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )
    matcher4 = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )
    matcher5 = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )
    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher):
        print(player)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))




if __name__ == "__main__":
    main()
