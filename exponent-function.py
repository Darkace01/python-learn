
def raise_to_power(base_num, pow_num):
    result = 1
    for _ in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3)) # 8