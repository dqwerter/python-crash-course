def describe_pet(annimal_type, pet_name):
    print('\nI have a ' + annimal_type + '.')
    print("My " + annimal_type.title() + "'s name is " + pet_name.title() + ".")

# identical 
describe_pet('hamster', 'harry')
describe_pet(annimal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', annimal_type='hamster')

# the order of parameters have changed
# parameters with default value must on tail
def describe_pet_default_parameter(pet_name, annimal_type='dog'):
    print('\nI have a ' + annimal_type + '.')
    print("My " + annimal_type.title() + "'s name is " + pet_name.title() + ".")

describe_pet_default_parameter('willie')
describe_pet_default_parameter('willie', 'dog')

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' +  middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

print(get_formatted_name('jimi', 'hendrix'))
print(get_formatted_name('john', 'hooker', 'lee'))
print('\n')

def print_models(unprinted_designs, completed_models):
    '''some description'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''some description'''
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

def show_unprinted_designs(unprinted_designs):
    '''some description'''
    print('\nThe following designs should be printed:')
    for unprinted_design in unprinted_designs:
        print(unprinted_design)

# called by address
unprinted_designs = ['phone', 'robot', 'printer']
completed_models = []
print_models(unprinted_designs, completed_models)
show_unprinted_designs(unprinted_designs)
show_completed_models(completed_models)

# called by value
unprinted_designs = ['phone', 'robot', 'printer']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_unprinted_designs(unprinted_designs)
show_completed_models(completed_models)

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print('')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)