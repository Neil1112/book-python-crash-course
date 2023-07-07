from admin import Admin

admin = Admin('John', 'Doe', age=30, location='New York', occupation='Programmer')
admin.describe_user()
admin.privileges.show_privileges()
