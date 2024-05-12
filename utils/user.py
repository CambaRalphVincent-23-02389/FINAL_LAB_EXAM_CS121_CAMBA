import os
class User:
    def __init__(self, username, password, score):
        self.username = username
        self.password = password
        self.score = score

    def load_users(self):
        user_file_path = os.path.join('data', 'user_credential.txt')
        users = []
        if os.path.exists(user_file_path):
            with open(user_file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split(',')
                    username = parts[0]
                    password = parts[1]
                    scores = int(parts[2])
                    users.append((username, password, scores))
        return users

    def save_users(self):
        user_folder = 'data'
        user_file_path = os.path.join(user_folder, 'user_credentials.txt')
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)
        with open(user_file_path, 'a+') as file:
            file.write(f"{self.username}, {self.password}, {self.score}\n")


