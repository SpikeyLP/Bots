class Bot:
    #1 steal 
    #0 split
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.history = []

    def choose(self, current_round, prev_round, prev_opponent_choice):
        if prev_opponent_choice != None:
            return 1 - prev_opponent_choice
        else :
            return 1