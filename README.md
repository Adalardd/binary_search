Функция ***binary_search*** получает отсортированный массив и значение. Если значение присутствует в массиве, то функция возвращает его позицию. При этом мы должны следить за тем, в какой части массива проводится поиск.

Вначале это весь массив:
    
    low = 0
    high = len(list) - 1

Каждый раз алгоритм проверяет средний элемент:

    mid = (low + high) / 2
    guess = list[mid]

Если значение *(low+high)* нечетное, то Python автоматически округляет значение mid в меньшую сторону.

Если названное число было слишком мало, то переменная *low* обновляется соответственно:

    if guess < item:
        low = mid + 1

А если догадка была слишком велика, то обновляется переменная *high*.         