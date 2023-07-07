class User:
    
    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = kwargs
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Login attempts: {self.login_attempts}")
        for key, value in self.user_info.items():
            print(f"\t{key}: {value}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
    


user_0 = User('John', 'Doe', age=30, location='New York', occupation='Programmer')

user_0.greet_user()
user_0.describe_user()
print('\n')

print(f"Login attempts: {user_0.login_attempts}")
print("Incrementing login attempts 2 times...")
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(f"Login attempts: {user_0.login_attempts}")
print("Resetting login attempts...")
user_0.reset_login_attempts()
print(f"Login attempts: {user_0.login_attempts}")