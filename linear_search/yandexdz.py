#возрастает ли список 
def growing_list(seq): 
    count = 0 #счетчик возрастания 
    for i in range(1, len(seq)): #можем не проверят первый элемент, перед ним ничего нет
        if seq[i] > seq[i - 1]: 
            count += 1
    if len(seq) - 1 == count: #проверяем совпадает ли количество элементов с возраст элементами
        return 'YES'
    else: 
        return 'NO'
    
seq = list(map(int, input.split()))
growing_list(seq)

#ближайшее число 

def near_number(seq, x):
    answer = seq[0] #берем как начальный ответ первый элемент
    min_diff = abs(seq[0] - x)#минимальная разница, берем разницу с первым элементом
    
    for i in seq[1:]:#от второго до конца последовательности, тк первый мы брали за начальный ответ
        diff = abs(i - x) #разница на текущей итерации, то есть между i и искомым числом
        if diff < min_diff: #если текущая разница меньше минимальной
            min_diff = diff #минимальная становится текущей(элемент который сейчас считаем минимальной разницей)
            answer = i #записываем в ответ текущий элемент
    return answer
            
            
    
    
    
    
n = int(input())# количество элементов последовательности
seq = list(map(int, input()))#считываем последовательность
x = int(input())

#больше своих соседей 

def bigger_then_neighbour(seq):
    ans = 0
    for i in range(1, len(seq) - 1): 
        if seq[i] > seq[i - 1] and seq[i] > seq[i + 1]: 
            ans += 1 
    return ans
    
    
    
seq = list(map(int, input().split()))
print(bigger_then_neighbour(seq))


#чемпионат лепешек

def place_of_lepeshka(seq):
    position_v = -1  # начальная позиция Василия (если не найдём, останется -1)
    res_v = 0        # результат лучшего броска Василия
    
    # Ищем Василия: его бросок оканчивается на 5, и следующий бросок меньше
    for i in range(len(seq) - 1):  # до предпоследнего элемента, чтобы не выйти за границы
        if seq[i] % 10 == 5 and seq[i + 1] < seq[i]:
            # Если это первый подходящий Василий или он сильнее предыдущих кандидатов
            if position_v == -1 or seq[i] > res_v:
                position_v = i
                res_v = seq[i]
    
    # Если Василий не найден
    if position_v == -1:
        return 0
    
    # Проверяем, был ли до Василия хотя бы один победитель (бросил строго дальше)
    has_winner_before = False
    for i in range(position_v):
        if seq[i] > res_v:
            has_winner_before = True
            break
    
    # Если до Василия не было никого, кто бросил строго дальше
    if not has_winner_before:
        return 0
    
    # Считаем количество участников, которые бросили строго дальше Василия
    count = 0
    for num in seq:
        if num > res_v:
            count += 1
    
    # Место Василия = количество более дальних бросков + 1
    return count + 1

n = int(input())
seq = list(map(int, input().split()))
print(place_of_lepeshka(seq))

