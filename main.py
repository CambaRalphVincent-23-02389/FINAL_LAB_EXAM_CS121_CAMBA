from utils.user_manager import UserManager
from utils.dice_game import DiceGame

# Main menu which focuses on user authentication and program entry
def main():
    user_manager = UserManager()
    dice_game = DiceGame()
    while True:
        print("\nWelcome to Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            user_manager.register()
        elif choice == '2':
            logged_user = user_manager.login()
            if logged_user:
                dice_game.menu(logged_user)
        elif choice == '3':
            exit()
        else:
            print("\nInvalid input. Please enter a valid input.")

if __name__ == '__main__':
    main()




