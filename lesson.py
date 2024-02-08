def outer(par):
    loc = par
    def inner():
        return loc
    return inner

let = 1
fun = outer(let)
print(fun())

print("")
print("________________________________________________")
print()

def make_closure(par):
    loc = par
    # Вложенная функция power, которая использует значение loc из "make_closure"
    def power(p):
        return p ** loc
    return power

# Создаем две замыкания с разными значениями loc (2 и 3)
fsqr = make_closure(2)  # Функция возведения в квадрат
fcub = make_closure(3)  # Функция возведения в куб

# Вызываем каждую из созданных функций для значений от 0 до 9
for i in range(1, 10 + 1):
    print()
    print(i, fsqr(i), fcub(i))  # Выводим результаты возведения в квадрат и в куб для каждого числа от 0 до 10
    
    
    
