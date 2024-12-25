from collections import defaultdict #Моя прелесть

import time
def can_connect(first, second):
    """
    Перевіряє, чи можна з'єднати два фрагменти.
    З'єднання можливе, якщо останні 2 цифри першого фрагмента співпадають з першими 2 цифрами другого.
    """
    return first[-2:] == second[:2]


def find_longest_puzzle(numbers):
    """
    Знаходить найдовшу послідовність фрагментів.
    """
    # Словник за першими 2 цифрами
    fragments_by_start = defaultdict(list)
    for number in numbers:
        fragments_by_start[number[:2]].append(number)

    def backtrack(current_puzzle, used_numbers):
        # фрагменти для соидинения
        possible_next = fragments_by_start.get(current_puzzle[-2:], [])

        # якщо немає вертаємось
        if not possible_next:
            return current_puzzle, used_numbers

        longest_puzzle = current_puzzle  # Поточна найдовша послідовність
        best_used = used_numbers  # Поточні використані числа

        # перебор варіанстів
        for next_number in possible_next:
            if next_number not in used_numbers:
                # Рекурсивно спробуємо додати наступне число
                new_puzzle = current_puzzle + next_number[2:]
                new_used = used_numbers + [next_number]

                # Рекурсия :(
                result_puzzle, result_used = backtrack(new_puzzle, new_used)


                if len(result_puzzle) > len(longest_puzzle):
                    longest_puzzle = result_puzzle
                    best_used = result_used

        return longest_puzzle, best_used

    # Починаємо з кожного числа і шукаємо найдовший ланцюжок
    longest_puzzle = ""
    best_used = []
    for number in numbers:
        result_puzzle, result_used = backtrack(number, [number])
        if len(result_puzzle) > len(longest_puzzle):
            longest_puzzle = result_puzzle
            best_used = result_used

    # Знаходимо невикористані числа
    unused_numbers = [num for num in numbers if num not in best_used]

    return longest_puzzle, unused_numbers

 # main

filename = "numbers.txt"
# Файл
with open(filename, 'r') as f:
    numbers = [line.strip() for line in f.readlines()]
#Время
start_time = time.time()
# Знаходимо найдовшу послідовність
longest_puzzle, unused_numbers = find_longest_puzzle(numbers)
end_time = time.time()
execution_time = end_time - start_time
# Виводимо результат
print(f"Найдовша послідовність: {longest_puzzle}")
print(f"Невикористані числа: {unused_numbers}, \n {len(unused_numbers)}") #75
print(f"Час виконання: {execution_time:.2f} секунд") # n
