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


class Privileges:
    
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")


class Admin(User):
            
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])


admin = Admin('John', 'Doe', age=30, location='New York', occupation='Programmer')
admin.describe_user()
admin.privileges.show_privileges()

