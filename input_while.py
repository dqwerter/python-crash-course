print("<--- Program 1 Flag Variable --->")
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

print("\n<--- Program 2 Structure Processing --->")
unconfirmed_users = ['alice', 'brian', 'candace']
confired_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confired_users.append(current_user)

print('\nThe following users have been confirmed:')
for confired_user in confired_users:
    print(confired_user.title())