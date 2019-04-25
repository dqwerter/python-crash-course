motorcycles = ["suzuki", "bmw", "yamaha"]
print(motorcycles)
print(motorcycles[0].title())
print(motorcycles[-1])
print("my first motorcycle was a " + motorcycles[0].title() + ".")

# modify elements
motorcycles[0] = "honda"
print(motorcycles)

# add
motorcycles.append("suzuki")
motorcycles.insert(0, "benz")
print(motorcycles)

# delete
del motorcycles[0]
print(motorcycles)
print(motorcycles.pop())
print(motorcycles)
print(motorcycles.pop(1))
print(motorcycles)
motorcycles.remove("yamaha")
print(motorcycles)
print('\n')

cars = ['bmw', 'audi', 'benz', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)
cars.sort()
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(len(cars))
