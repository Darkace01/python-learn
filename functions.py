def say_hi():
    print('Hello User')

print('Top')
say_hi()
print('Bottom')


def say_hi(name, age):
    print('Hello ' + name + ', you are ' + age)

say_hi('Mike', "35")


# Return Statement

def cube(num):
    return num*num*num

result = cube(4)
print(result)


# If Statements

is_male = True
is_tall = True

if is_male or is_tall:
    print('You are a male or tall or both')
else:
    print('You are neither male or tall')


if is_male and is_tall:
    print('You are a tall male')
elif is_male and not(is_tall):
    print('You are a short male')

elif not(is_male) and is_tall:
    print('You are not a male but are tall')
else:
    print('You are either mot male or tall or both')


# If Statements & Comparisons
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
print(max_num(3,4,5))