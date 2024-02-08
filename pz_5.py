import random


def find_min_sum_sequence(sequence, start_index = 0, current_min = float('inf'), position = 0):
    if start_index + 10 >= len(sequence):
        return position
    
    sum_current = sum(sequence[start_index:start_index + 10])
    
    if sum_current < current_min:
        current_min = sum_current
        position = start_index
    return find_min_sum_sequence(sequence, start_index + 1, current_min, position)

# Список из случайных чисел
array = [random.randint(1, 1000) for _ in range(100 + 1)]

print(array)
print()
resault = find_min_sum_sequence(array)
print(resault)