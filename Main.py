import random
import pandas as pd
from Game import Game
from Team import Team

SeniorGamesList = []
Senior1Teams = []
Senior2Teams = []
JuniorTeams = []
SeniorParks = ["Parkway Forest", "Wigmore", "Iroquois", "Hobart", "Warden"]
weekends = pd.bdate_range(start="2023/05/27", end="2023/08/13", freq="C", weekmask="Sat Sun")


def parkSetup():
    for date in weekends:
        stringDate = (str(date).split()[0])
        # Filter Canada Day, Father's Day, Civic Holiday Weekend 2023
        if stringDate == "2023-07-01" or stringDate == "2023-07-18" or stringDate == "2023-08-05" or stringDate == "2023-08-06":
            continue
        else:
            for park in SeniorParks:
                for time in range(2, 8, 2):
                    stringTime = str(time)
                    SeniorGamesList.append(Game(stringDate, stringTime, park))

    count = 0
    for games in SeniorGamesList:
        count += 1
        print(games.__str__())
    print(str(count) + " senior games can be played")


def teamSetup():
    with open("teams.txt") as file:
        for line in file:
            splitLine = line.rstrip().split(maxsplit=2)
            if splitLine[1] == "S1":
                Senior1Teams.append(Team(splitLine[0], splitLine[1], splitLine[2]))
            elif splitLine[1] == "S2":
                Senior2Teams.append(Team(splitLine[0], splitLine[1], splitLine[2]))

    for team in Senior1Teams:
        print(team)
    for team2 in Senior2Teams:
        print(team2)


def gameSetup():
    # Umped games setup

    pass
    # RESTRICTIONS
    # 5 home, 5 away, 10 games
    # if playing one day, dont let them play at different parks at different times on that day
    # some teams no double headers, no 2pm 6pm double headers or at different parks
    # no same church matchup
    # no play dates
    # spread games as much as possible


def main():
    parkSetup()
    teamSetup()
    gameSetup()


if __name__ == '__main__':
    main()
