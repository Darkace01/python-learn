for letter in "Giraffe Academy":
    print(letter)


# For with arrays
friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

# For with range
for index in range(3,10):
    print(index)

length = len(friends)

# array with index
for index in range(length):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print("Not first")