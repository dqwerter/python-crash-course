'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''

filename = 'pi_digits.txt'
with open(filename) as file_object_1:
    for line in file_object_1:
        print(line.rstrip())            # use rstrip rather than strip

filename = 'pi_million_digits.txt'
with open(filename) as file_object_2:
    lines = file_object_2.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print('Len of the digits printed above: ' + str(len(pi_string)) + '\n')

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
