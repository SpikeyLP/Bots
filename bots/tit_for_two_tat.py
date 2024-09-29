class Bot:
    #1 steal 
    #0 split
    def __init__(self, name, totround):
        self.name = name
        self.score = 0
        self.history = []
        self.totround = totround

    def choose(self, current_round, prev_round, prev_opponent_choice):
        if prev_opponent_choice == None or len(history) < 2:  # too early
            return 0

        if self.history[-2][1] == 1 and self.history[-1][1] == 1:  # opponent stole twice
            return 1

        if current_round == self.totround:  # last round
            return 1  # no point in splitting

        return 0  # split by default
