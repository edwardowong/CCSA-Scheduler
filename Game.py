class Game:
    date = ""
    time = ""
    home = ""
    away = ""
    ump = ""
    location = ""

    def __init__(self, date, time, location):
        self.date = date
        self.time = time
        self.location = location

    def getDate(self):
        return str(self.date)

    def getTime(self):
        return str(self.time)

    def getLocation(self):
        return self.location

    def setGame(self, home, away, ump):
        self.home = home
        self.away = away
        self.ump = ump

    def setUmp(self, ump):
        self.ump = ump

    def isEmpty(self):
        if self.home != "":
            return False
        return True

    def __str__(self):
        return str(self.home) + " plays " + str(self.away) + ", umped by " + str(self.ump) + " at " + \
            str(self.location) + " on " + str(self.date) + " at " + str(self.time) + " pm."



