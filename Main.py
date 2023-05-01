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
        formattedDate = "".join(stringDate.split('-'))
        # Filter Canada Day, Father's Day, Civic Holiday Weekend 2023
        if formattedDate == "20230701" or formattedDate == "20230718" or formattedDate == "20230805" or formattedDate == "20230806":
            continue
        else:
            for park in SeniorParks:
                for time in range(2, 8, 2):
                    stringTime = str(time)
                    SeniorGamesList.append(Game(formattedDate, stringTime, park))

    # count = 0
    # for games in SeniorGamesList:
    #     count += 1
    #     print(games.__str__())
    # print(str(count) + " senior games can be played")


def teamSetup():
    with open("teams.txt") as file:                     # Add CCSA teams to a list
        for line in file:
            splitLine = line.rstrip().split(maxsplit=2)
            if splitLine[1] == "S1":
                Senior1Teams.append(Team(splitLine[0], splitLine[1], splitLine[2]))
            elif splitLine[1] == "S2":
                Senior2Teams.append(Team(splitLine[0], splitLine[1], splitLine[2]))

    file = pd.read_csv("Sr NPD.csv")
    filterHeader = file.columns.str.contains("reason")
    reasonList = (file.columns[filterHeader].to_list())
    fileNoReasonList = file.loc[:, ~file.columns.isin(reasonList)]
    fileOnlyPlayDates = fileNoReasonList.loc[:, ~fileNoReasonList.columns.isin(['details', 'fnpd_id', 'pref-double-header-games', 'pref-triple-header-ump', 'submission_time', 'submitter_email', 'submitter_name', 'submitter_playerid',  'teamid'])]
    meltedFile = pd.melt(fileOnlyPlayDates, id_vars="teamname", var_name="Date", value_name="Play")
    noPlayFile = meltedFile[meltedFile['Play'].str.contains('no', na=False)]
    noPlayFile["Time"] = noPlayFile["Date"].str[-1:]
    noPlayFile["Date"] = noPlayFile["Date"].str[0:8]

    for index, row in noPlayFile.iterrows():
        team = next((S1Team for S1Team in Senior1Teams if S1Team.name == row["teamname"]), None)  # Find team object from S1 list using team name
        if team is None:
            team = next((S2Team for S2Team in Senior2Teams if S2Team.name == row["teamname"]), None)  # Find team object from S2 list using team name
        for game in SeniorGamesList:
            if game.date == row["Date"] and game.time == row["Time"]:
                team.setNoPlayDate(game)

    # Testing, this will print game objects that are no play dates for a specific team
    team = next(S1Team for S1Team in Senior1Teams if S1Team.name == "Resonate")
    for games in team.no_play_date_list:
        print(games)

    # for team in Senior1Teams:
    #     print(team)
    # for team2 in Senior2Teams:
    #     print(team2)
    # print("Senior teams:", len(Senior1Teams) + len(Senior2Teams))


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
