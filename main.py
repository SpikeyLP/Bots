import os
import importlib

output = 0

class Game:
    def __init__(self):
        self.bots = self.load_bots()

    def load_bots(self):
        bot_folder = 'bots'
        bot_files = [f[:-3] for f in os.listdir(bot_folder) if f.endswith('.py') and f != '__init__.py']
        bots = []
        for bot_file in bot_files:
            module_name = f'bots.{bot_file}'
            bot_module = importlib.import_module(module_name)
            bot_class = getattr(bot_module, 'Bot')
            bots.append(bot_class(bot_file))  # Initialize each bot
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

    def simulate_game(self, bot1, bot2, rounds=8):
        for round_num in range(1, rounds + 1):
            self.play_round(bot1, bot2, round_num)
        if output == 1:
            # Print final score for each match
            print(f"({bot1.name}) total = {bot1.score}")
            print(f"({bot2.name}) total = {bot2.score}\n")

    def simulate_round_robin(self, rounds=8):
        num_bots = len(self.bots)
        for i in range(num_bots):
            for j in range(i + 1, num_bots):
                if output == 1:
                   print(f"\nMatch: {self.bots[i].name} vs {self.bots[j].name}")
                self.simulate_game(self.bots[i], self.bots[j], rounds)

        # Print total scores after all matches, sorted from lowest to highest
        self.print_total_scores()

    def print_total_scores(self):
        print("\nFinal total scores (sorted from lowest to highest):")
        # Sort bots by their score in ascending order
        sorted_bots = sorted(self.bots, key=lambda bot: bot.score)
        for bot in sorted_bots:
            print(f"({bot.name}) total = {bot.score}")

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
