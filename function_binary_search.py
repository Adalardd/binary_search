def binary_search(list, item):
    '''Функция binary_search получает отсортированный массив и значение и возвращает позицию этого значения в массиве.'''
    
    low = 0 # начало массива
    high = len(list) - 1 # конец массива

    while low <= high: # пока эта часть не сократится до одного элемента
        mid = int((low + high) / 2) # проверяем средний элемент
        guess = list[mid]
        if guess == item: # значение найдено
            return mid
        elif guess > item: # много
            high = mid - 1
        else: # мало
            low = mid + 1
    return None # значение не найдено

my_list = [1, 3, 5, 7, 9] # тестовый массив

print(binary_search(my_list, 3)) # должно вернуть 1
print(binary_search(my_list, -1)) # должно вернуть None


