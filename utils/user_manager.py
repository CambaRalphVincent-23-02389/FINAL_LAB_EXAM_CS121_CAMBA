import os
from utils.user import User
class UserManager:
	def __init__(self):
		self.data_folder = 'data'
		self.user_credentials_file = os.path.join(self.data_folder, 'user_credentials.txt')


	# Checks username input if already exists
	def check_username(self, username):
		with open(self.user_credentials_file, 'r') as file:
			for line in file:
				stored_username, stored_password, score = line.strip().split(',')
				if username == stored_username:
					return True
		return False


	# This method checks the username and password if it exists and correct
	def check_user_credentials(self, username, password):
		with open(self.user_credentials_file, 'r') as file:
			for line in file:
				stored_username, stored_password, score = line.strip().split(', ')
				if username == stored_username and password == stored_password:
					return True
		return False

	# Allows users to register
	def register(self):
		print("\n--REGISTER--")
		username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
		if not username:
			return
		if len(username) < 4:
			print("Username must be at least 4 characters.")
			self.register()
		else:
			if self.check_username(username):
				print("Username already exists. Please try other username.")
			else:
				password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
				if not password:
					return
				if len(password) < 8:
					print("Password must be at least 8 characters long.")
					self.register()
				else:
					user = User(username, password, 0)
					user.save_users()
					print("Registered successfully.")

	# Allows the user to log in
	def login(self):
		print("\n--LOGIN--")
		username = input("Enter username (at least 4 characters): ")
		password = input("Enter password (at least 8 characters): ")
		user = User(username, password, 0)
		if self.check_user_credentials(username, password):
			print("\nLogin successfully.")
			return user
		print("Incorrect username or password.")
		return None











