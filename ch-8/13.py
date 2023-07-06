def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile_0 = build_profile('albert', 'einstein', location='princeton', field='physics', known_for='theory of relativity')
user_profile_1 = build_profile('issac', 'newton', location='england', field='physics', known_for='gravity')

print(user_profile_0)
print(user_profile_1)