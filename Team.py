class Team:
    church = ""
    division = ""
    name = ""
    no_play_date = ""
    no_play_time = ""
    doubleheader = ""
    currentGames = 0
    maxPlayedGames = 10
    maxUmpedGames = 6

    def __init__(self, church, division, name):
        self.church = church
        self.division = division
        self.name = name

    def getChurch(self):
        return self.church

    def getNoPlayDates(self):
        return self.no_play_date

    def getNoPlayTime(self):
        return self.no_play_time

    def __str__(self):
        return str(self.church) + " " + str(self.name)
