import os
import importlib

output = 1  # Change this to 0 if you don't want any print statements.

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

    def print_totround(self):
        print(f"{self.name} - Total Rounds: {self.totround}")  # Method to print the total rounds

class Game:
    def __init__(self):
        self.totround = 40  # Set total rounds here
        self.bots = self.load_bots()  # Load bots after defining totround

    def load_bots(self):
        bot_folder = 'bots'
        bot_files = [f[:-3] for f in os.listdir(bot_folder) if f.endswith('.py') and f != '__init__.py']
        bots = []
        for bot_file in bot_files:
            module_name = f'bots.{bot_file}'
            bot_module = importlib.import_module(module_name)
            bot_class = getattr(bot_module, 'Bot')
            bots.append(bot_class(bot_file, self.totround))  # Pass totround to each bot
        return bots

    def play_round(self, bot1, bot2, round_num):
        if round_num == 1:
            bot1_choice = bot1.choose(round_num, None, None)
            bot2_choice = bot2.choose(round_num, None, None)
        else:
            prev_bot1_choice, prev_bot2_choice = bot1.history[-1]
            bot1_choice = bot1.choose(round_num, round_num - 1, prev_bot2_choice)
            bot2_choice = bot2.choose(round_num, round_num - 1, prev_bot1_choice)

        # Update scores
        if bot1_choice == 0 and bot2_choice == 0:
            bot1.score += 10
            bot2.score += 10
        elif bot1_choice == 1 and bot2_choice == 1:
            bot1.score += 0
            bot2.score += 0
        elif bot1_choice == 0 and bot2_choice == 1:
            bot1.score += 0
            bot2.score += 20
        elif bot1_choice == 1 and bot2_choice == 0:
            bot1.score += 20
            bot2.score += 0

        # Update history
        bot1.history.append((bot1_choice, bot2_choice))
        bot2.history.append((bot2_choice, bot1_choice))

        # Print scores for the current round
        print(f"Round {round_num}: ({bot1.name}) = {bot1.score}, ({bot2.name}) = {bot2.score}")

    def simulate_game(self, bot1, bot2, rounds):
        for round_num in range(1, rounds + 1):
            self.play_round(bot1, bot2, round_num)

        # Print final score for each match
        print(f"Final score for match ({bot1.name}) vs ({bot2.name}): {bot1.score} - {bot2.score}\n")

    def simulate_round_robin(self):
        num_bots = len(self.bots)
        rounds = 4  # Starting rounds
        while rounds <= self.totround:
            for i in range(num_bots):
                for j in range(i + 1, num_bots):
                    if output == 1:
                        print(f"\nMatch: {self.bots[i].name} vs {self.bots[j].name} (Rounds: {rounds})")
                    self.simulate_game(self.bots[i], self.bots[j], rounds)
            rounds += 4  # Increment rounds by 4

        # Print total scores after all matches, sorted from lowest to highest
        self.print_total_scores()

    def print_total_scores(self):
        print("\nFinal total scores (sorted from lowest to highest):")
        # Sort bots by their score in ascending order
        sorted_bots = sorted(self.bots, key=lambda bot: bot.score)
        total_scores = sum(bot.score for bot in sorted_bots)  # Sum of all scores
        for bot in sorted_bots:
            print(f"({bot.name}) total = {bot.score}")
        print(f"Total score of all bots = {total_scores}")

    def reset_scores(self):
        # Method to reset all bot scores and history
        for bot in self.bots:
            bot.score = 0
            bot.history = []
        print("Scores have been reset!")

if __name__ == "__main__":
    game = Game()

    if len(game.bots) < 2:
        print("Need at least two bots to play!")
    else:
        # Play a round-robin tournament where each bot plays against every other bot
        game.simulate_round_robin()

        # Optionally reset scores (you can add user input to trigger this)
        # game.reset_scores()
