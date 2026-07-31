def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
    

print(raise_to_power(3, 3))




def divide(base_num, div_num):
    result = 1
    for index in range(div_num):
        result = result / base_num
    return result


print(divide (8, 2))