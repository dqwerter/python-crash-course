cars = ['audi', 'bmw', 'benz', 'sibaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

if 'audi' in cars:
    print('I have an Audi.')
if 'porshe' not in cars:
    print("I don't have a Porshe")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print(price)

