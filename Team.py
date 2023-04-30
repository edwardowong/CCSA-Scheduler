class Team:

    def __init__(self, church, division, name):
        self.church = church
        self.division = division
        self.name = name
        self.no_play_date_list = []
        self.game_list = []
        self.currentPlayed = 0
        self.maxPlayedGames = 10
        self.currentUmped = 0
        self.maxUmpedGames = 5

    def getChurch(self):
        return self.church

    def getCurrentUmped(self):
        return self.currentUmped

    def getGamesPlayed(self):
        return self.currentPlayed

    def setGame(self, game):
        self.game_list.append(game)
        self.currentPlayed += 1

    def setUmpedGame(self, gamesList, date):
        for game in gamesList:                          # Umps will not play games on days they ump
            if game.getDate() == date:
                self.no_play_date_list.append(game)
        self.currentUmped += 1

    def canUmp(self, date):
        for noPlayDates in self.no_play_date_list:      # Umps will not ump on no play dates
            if noPlayDates == date:
                return False
        if self.currentUmped >= self.maxUmpedGames:     # Umps will not ump more than the max umped games
            return False
        return True

    def __str__(self):
        return str(self.church) + " " + str(self.name)
