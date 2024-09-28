class Bot:
    #1 steal 
    #0 split
    def __init__(self, name, totround):
        self.name = name
        self.score = 0
        self.history = []
        self.times_opponent_stole = 0  # Instance variable
        self.totround = totround

    def choose(self, current_round, prev_round, prev_opponent_choice):
        if prev_opponent_choice == 1:
            self.times_opponent_stole += 1  
        if self.times_opponent_stole >= (self.totround / 4):
            return 1
        else:
            return 0