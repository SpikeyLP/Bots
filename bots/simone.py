class Bot:
    #1 steal 
    #0 split
    def __init__(self, name, totround):
        self.name = name
        self.score = 0
        self.history = []
        self.totround = totround

    def choose(self, current_round, prev_round, prev_opponent_choice):
        return 1  # Always steal
