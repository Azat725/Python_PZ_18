def func(length_of_stars):
    for _ in range(length_of_stars):
        print("*", end='')    
    print()

# length_of_stars = input("Введите количество звездочек >>> ")

n = func(5)
print(n)