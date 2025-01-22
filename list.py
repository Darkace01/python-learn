friends = ['Joseph', 'Glenn', 'Sally', 'Jen', 'Karen']
print(friends)
print(friends[1:])
print(friends[1:3])

print(friends[1])
friends[1] = 'Mike'
print(friends[1])

friends.pop()

print(friends.index('Sally'))
print(friends.count('Sally'))

friends.sort()
print(friends)

friends.reverse()
print(friends)

friends2 = friends.copy()
print(friends2)