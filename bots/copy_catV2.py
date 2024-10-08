class Bot:
    # 1 = steal 
    # 0 = split
    def __init__(self, name, totround):
        self.name = name
        self.score = 0
        self.history = []
        self.totround = totround  # Initialize totround here

    def choose(self, current_round, prev_round, prev_opponent_choice):
        if prev_opponent_choice is not None:
            return 1 - prev_opponent_choice  # Opponent's last choice: steal if they split, split if they steal
        else:
            return 1  # Default choice: steal on the first round