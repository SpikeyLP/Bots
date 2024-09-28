class Bot:
    #1 steal
    #0 share
    def __init__(self, name, totround):
        self.name = name
        self.score = 0
        self.history = []
        self.max_history = 2 # max prev moves to look at
        self.prev_opp_2_moves = [] # storing previous moves
        self.fool_me_twice = 0 # prevent letting the opponent get the advantage
        self.totround = totround

    def choose(self, current_round, prev_round, prev_opponent_choice):
        if prev_opponent_choice != None:
            self.append_last_moves(prev_opponent_choice)

        return self.make_choice()

    # append last move to previous moves list
    def append_last_moves(self, prev_opponent_choice):
        if len(self.prev_opp_2_moves) < self.max_history:
            self.prev_opp_2_moves.append(prev_opponent_choice)
        else:
            # remove oldest entry in previous moves list if list is longer than max_history
            self.prev_opp_2_moves.pop(0)
            self.prev_opp_2_moves.append(prev_opponent_choice)
    
    def make_choice(self):
        trust_score = 0 # how many times the opponent stole
        for move in self.prev_opp_2_moves:
            if move == 1:
                trust_score += 1

        # stop trusting opponent if they have stolen max_history amount of times more than once
        # score is higher without this but we get taken advantage of more often
        # this gives a higher rank
        if self.fool_me_twice == 2:
            return 1
        
        # Betting that the opponent won't steal again if they have already stolen max_history amount of times
        # Stealing if the opponent is not stealing (opportunist)
        if trust_score == self.max_history:
            self.fool_me_twice += 1
            return 0
        else:
            return 1
