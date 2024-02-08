def main_func(a, b):
    first_num = a
    second_num = b
    def inner_func():
        resault = 0
        for i in range(first_num, second_num + 1):
                resault += i
        return resault
    return inner_func

# a = 3
# b = 7

a = int(input("Enter a first num >>>  "))
b = int(input("Enter a second num >>>  "))

sum_in_range = main_func(a, b)
print(sum_in_range())