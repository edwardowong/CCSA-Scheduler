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

    def set_game(self, home, away, ump):
        self.home = home
        self.away = away
        self.ump = ump

    def is_empty(self):
        if self.home != "":
            return False
        return True

    def __str__(self):
        return str(self.home) + " plays " + str(self.away) + ", umped by " + str(self.ump) + " at " + \
            str(self.location) + " on " + str(self.date) + " at " + str(self.time) + " pm."



