magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("Can't wait to see the next, " + magician.title() + ".")
print("Thank you everyone!\n")

nums = []
for value in range(0, 11):
    nums.append(value**2)
print(nums)
min(nums)
max(nums)
sum(nums)
nums = [value**2 for value in range(0, 10)]
print(nums)

even_nums = list(range(1, 11, 2))
print(even_nums)

print("Sum of 1:1000000: ")
million_nums = list(range(1, 1000001))
# print(million_nums)
print(min(million_nums))
print(max(million_nums))
print(sum(million_nums))

cube_nums = [value**3 for value in range(1, 11)]
print(cube_nums)

players = ['charles', 'martina', 'micheal', 'florence', 'eli']
print(players[1:4])

for player in players[:3]:
    print(player)

good_players = players[:]
player = []
print(good_players)
