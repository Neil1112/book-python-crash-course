class User:
    
    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = kwargs

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        for key, value in self.user_info.items():
            print(f"\t{key}: {value}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")


user_0 = User('John', 'Doe', age=30, location='New York', occupation='Programmer')
user_1 = User('Jane', 'Doe', age=25, location='New York', occupation='Teacher')
user_2 = User('Jack', 'Doe', age=15, location='New York', occupation='Student')

user_0.greet_user()
user_0.describe_user()
print('\n')

user_1.greet_user()
user_1.describe_user()
print('\n')

user_2.greet_user()
user_2.describe_user()