import os
import random
from utils.user import User
from utils.score import ScoreMixin
from datetime import datetime

class DiceGame(ScoreMixin):
    def __init__(self):
        self.user_main_score = 0
        self.user_total_stages_won = 0
        self.user_stages_won = 0
        self.current_stage = 1
        self.total_rounds = 3

        self.data_folder = 'data'
        self.score_file = os.path.join(self.data_folder, 'highest_score.txt')
        self.highest_score_date_file = os.path.join(self.data_folder, 'highest_score_date.txt')
        self.highes_score_holder_file = os.path.join(self.data_folder, 'highest_score_holder.txt')

        super().__init__(self.score_file)
        self.create_data_folder()


    # Create data folder if don't exist
    def create_data_folder(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    # Loads the highest score date
    def load_highest_score_date(self):
        if os.path.exists(self.highest_score_date_file):
            with open(self.highest_score_date_file, 'r') as file:
                return file.read()
        return None

    # Loads the username of the current highest score holder
    def load_highest_score_holder(self):
        if os.path.exists(self.highes_score_holder_file):
            with open(self.highes_score_holder_file, 'r') as file:
                return file.read()
        return None

    # After a game, it saves highest score, highest score date, and highest score holder
    def save_highest_score_and_date_and_holder(self, score, date, user):
        try:
            with open(self.score_file, 'w') as file:
                file.write(str(score))
            with open(self.highest_score_date_file, 'w') as file:
                file.write(date)
            with open(self.highes_score_holder_file, 'w') as file:
                file.write(user)
        except IOError:
            print("Error: Unable to save score and date.")

    # Starts the game
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
                    print("It's a TIE!")
                elif user_random_number > cpu_random_number:
                    print(f"{user.username} WON this round!")
                    user_sub_score += 1
                elif cpu_random_number > user_random_number:
                    print(f"{user.username} LOST this round!")


            if user_sub_score < 2:
                print(f"\nYou LOST this stage {user.username}.")
                if self.user_total_stages_won == 0:
                    print("GAME OVER. You didn't win any stages.")
                    print("To win a stage, you must have at least won two of the rounds, and if you win a stage, you will receive an additional 3 points.")
                    self.reset_user_records()
                    # self.menu(user)
                    break
                else:
                    print(f"Total points: {self.user_main_score}, Stages won: {self.user_total_stages_won}")
                    self.check_score(user)
                    self.reset_user_records()
                    # self.menu(user)
                    break

            else:
                in_game_stages_won += 1
                self.user_total_stages_won += in_game_stages_won
                stage_won_points = 3
                user_sub_score = user_sub_score + stage_won_points
                self.user_main_score = self.user_main_score + user_sub_score
                print(f"\nYou WON this stage {user.username}!")
                print(f"Total points: {self.user_main_score}, Stages won: {self.user_total_stages_won}")
                user_decision = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")

                if user_decision == "1":
                    self.current_stage += 1
                elif user_decision == "0":
                    print(f"Game over. You won {self.user_total_stages_won} stage(s) with a total of {self.user_main_score} points.")
                    self.check_score(user)
                    self.reset_user_records()
                    # self.menu(user)
                    break
                else:
                    print("Invalid input. Please enter 1 or 0.")
                    # self.menu(user)
                    continue

    # Resets score every game
    def reset_user_records(self):
        self.user_main_score = 0
        self.user_total_stages_won = 0
        self.user_stages_won = 0
        self.current_stage = 1

    # Checks if the user beats the highest score
    def check_score(self, user):
        highest_score = self.load_highest_score()
        highest_score_date = self.load_highest_score_date()
        highest_score_holder = self.load_highest_score_holder()
        if highest_score is None or self.user_main_score > highest_score:
            if highest_score is not None:
                print(f"NEW RECORD!!! By {user.username}! Previous record: {highest_score} Points (Achieved on: {highest_score_date})")
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_highest_score_and_date_and_holder(self.user_main_score, current_datetime, user.username)
        else:
            print(f"FAIL TO ACHIEVE NEW RECORD. CURRENT RECORD: {highest_score} Points (Achieved on: {highest_score_date})")

    # Shows the current highest score holder
    def show_highest_score(self, user):
        highest_score = self.load_highest_score()
        highest_score_date = self.load_highest_score_date()
        highest_score_holder = self.load_highest_score_holder()
        if highest_score is not None:
            print(f"\nCurrent Highest Score Holder: {highest_score_holder}, {highest_score} Points (Achieved on: {highest_score_date})")
        else:
            print("\nNo highest score recorded yet.")

    # Logout the user and returns to main menu
    def logout(self, user):
        print(f"\nGoodbye {user.username}!")
        print("You logged out successfully.")
        return

    # Game menu that focuses on game interactions
    def menu(self, user):
        while True:
            print(f"\nWelcome to Dice Roll Game!, {user.username}!")
            print("1. Start Game")
            print("2. Show Highest Score Holder")
            print("3. Log Out")
            choice = input("Enter your choice: ")

            if not choice:
                continue
            if choice == '1':
                self.play_game(user)
            elif choice == '2':
                self.show_highest_score(user)
            elif choice == '3':
                self.logout(user)
                break
            else:
                print("Invalid input. Please enter a valid input.")