import os
import random
from utils.user import User

class DiceGame:
    def __init__(self):
        self.user_main_score = 0
        self.user_total_stages_won = 0
        self.user_stages_won = 0
        self.current_stage = 1
        self.total_rounds = 3

    def load_scores(self):
        pass

    def save_scores(self):
        pass

    def play_game(self, user):
        while True:
            user_sub_score = 0
            in_game_stages_won = 0

            print(f"\nStage {self.current_stage}")
            for x in range(self.total_rounds):
                user_random_number = random.randint(1,6)
                cpu_random_number = random.randint(1,6)
                print(f"{user.username} rolled: {user_random_number}")
                print(f"CPU rolled: {cpu_random_number}")

                if user_random_number == cpu_random_number:
                    print("It's a tie!")
                elif user_random_number > cpu_random_number:
                    print(f"{user.username} WON this round!")
                    user_sub_score += 1
                elif cpu_random_number > user_random_number:
                    print(f"{user.username} LOST this round!")


            if user_sub_score < 2:
                print(f"You lost this stage {user.username}")
                if self.user_total_stages_won == 0:
                    print("Game over. You didn't win any stages.")
                    self.user_main_score = 0
                    self.user_total_stages_won = 0
                    self.user_stages_won = 0
                    self.current_stage = 1
                    self.menu(user)
                else:
                    print(f"Total points: {self.user_main_score}, Stages won: {self.user_total_stages_won}")
                    self.user_main_score = 0
                    self.user_total_stages_won = 0
                    self.user_stages_won = 0
                    self.current_stage = 1
                    self.menu(user)
            else:
                in_game_stages_won += 1
                self.user_total_stages_won += in_game_stages_won
                stage_won_points = 3
                user_sub_score = user_sub_score + stage_won_points
                self.user_main_score = self.user_main_score + user_sub_score
                print(f"\nYou won this stage {user.username}!")
                print(f"{user.username}")
                print(f"Total points: {self.user_main_score}, Stages won: {self.user_total_stages_won}")
                user_decision = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")

                if not user_decision:
                    return
                if user_decision == "1":
                    self.current_stage += 1
                    self.play_game(user)
                elif user_decision == "0":
                    print(f"Game over. You won {self.user_total_stages_won} with a total of {self.user_main_score} points.")
                    self.user_main_score = 0
                    self.user_total_stages_won = 0
                    self.user_stages_won = 0
                    self.current_stage = 1
                    self.menu(user)

    def show_top_scores(self):
        pass

    def logout(self, user):
        print(f"\nGoodbye {user.username}!")
        print("You logged out successfully.")
        return

    def menu(self, user):
        while True:
            print(f"\nWelcome to Dice Roll Game!, {user.username}!")
            print("1. Start game")
            print("2. Show highest score holder")
            print("3. Logout")
            choice = input("Enter your choice: ")
            if not choice:
                return
            if choice == '1':
                self.play_game(user)
            elif choice == '2':
                pass
            elif choice == '3':
                self.logout(user)
            else:
                print("Invalid input. Please enter a valid input.")

