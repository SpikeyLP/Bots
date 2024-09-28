class Bot:
    #1 steal 
    #0 split
    def __init__(self, name, totround):
        self.name = name
        self.score = 0
        self.history = []
        self.times_opponent_split = 0
        self.totround = totround

    def choose(self, current_round, prev_round, prev_opponent_choice):
        if prev_opponent_choice == 0:
            self.times_opponent_split += 1  
        if current_round <= self.totround / 4:
            return 0
        elif current_round == self.times_opponent_split:
            if current_round <= self.totround *3 / 4:
                return 0
            else :
                return 1
        else:
            return 1