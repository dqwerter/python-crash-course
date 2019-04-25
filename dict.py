favorate_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print(favorate_languages['phil'])
favorate_languages['phil'] = 'go'
print(favorate_languages)
favorate_languages['daniel'] = 'java'
print(favorate_languages)
del favorate_languages['daniel']
print(favorate_languages)
print('')


for person, language in favorate_languages.items():
    print(person.title() + ' loves ' + language.title() + '.')
print('')

for person in favorate_languages.keys():
    print(person.title())
print('')

# indentical to .keys()
for person in favorate_languages:
    print(person.title())
print('')

for language in favorate_languages.values():
    print(language)
print('')

# sort by keys 
for person, language in sorted(favorate_languages.items()):
    print(person.title() + ' loves ' + language.title() + '.')
print('')

if 'daniel' not in favorate_languages.keys():
    print('Daniel, would you like to take a poll?')
print('')

favorate_languages['daniel'] = 'python'
print('Language mentioned:')
for language in set(favorate_languages.values()):
    print(language.title())

