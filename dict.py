favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(favorite_languages['phil'])
favorite_languages['phil'] = 'go'
print(favorite_languages)
favorite_languages['daniel'] = 'java'
print(favorite_languages)
del favorite_languages['daniel']
print(favorite_languages)
print('')


for person, language in favorite_languages.items():
    print(person.title() + ' loves ' + language.title() + '.')
print('')

for person in favorite_languages.keys():
    print(person.title())
print('')

# identical to .keys()
for person in favorite_languages:
    print(person.title())
print('')

for language in favorite_languages.values():
    print(language)
print('')

# sort by keys 
for person, language in sorted(favorite_languages.items()):
    print(person.title() + ' loves ' + language.title() + '.')
print('')

if 'daniel' not in favorite_languages.keys():
    print('Daniel, would you like to take a poll?')
print('')

favorite_languages['daniel'] = 'python'
print('Language mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())

