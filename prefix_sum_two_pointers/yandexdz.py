#A. Стильная одежда

#решение за O(n + m )  два указателя, тк 2 масисва отсортированы
def greates_pairs_clothes():
    N = int(input())  # вводим n
    shirts = list(map(int, input().split()))  # вводим массив футболок
    
    M = int(input())  # вводим m 
    pants = list(map(int, input().split()))  # вводим массив штанов
    
    i, j = 0, 0  # два указателя, оба на нулевой элемент
    best_pair = (shirts[0], pants[0])  # лучшая пара, изначально первые элементы (закрывает краевые варианты)
    min_diff = abs(shirts[0] - pants[0])  # начальная минимальная разница
    
    while i < N and j < M:  # пока не исчерпали длину
        shirt = shirts[i]  # текущая футболка
        pant = pants[j]  # текущие штаны
        diff = abs(shirt - pant)  # текущая разница между элементами
        
        if diff < min_diff:  # если текущая разница меньше минимальной
            min_diff = diff  # то минимальную обновляем, делаем текущей
            best_pair = (shirt, pant)  # лучшая пара становится текущей

        if diff == 0:  # если разница 0, заканчиваем цикл — лучше пары не будет
            break
        
        if shirt < pant:  # двигаем указатели, если текущая футболка меньше штанов
            i += 1  # то увеличиваем указатель у футболки, чтобы сократить разницу
        else: 
            j += 1  # иначе наоборот
            
    print(best_pair[0], best_pair[1])  # возвращаем пару 

greates_pairs_clothes()

# B. Сумма номеров
#задача на префиксные суммы 
#решение за O(n) time, space O(n)
def count_pairs_nomer():
    n, k = list(map(int, input().split()))#ввод количества и подходящего числа
    car_license_plates = list(map(int, input().split()))#ввод массива номеров
    count = 0#счетчик подотрезков
    current_sum = 0
    prefix_counts = {0: 1}  # сумма 0 уже есть (для подотрезков, начинающихся с нуля)
    #для счетчика количества вхождения преф сумм, ключ - преф сумма, значение - количество нахождения преф суммы
    
    for num in car_license_plates:#по массиву номеров
        current_sum += num#текущая сумма
        
        # Если раньше была сумма current_sum - k, то подотрезок с суммой k найден
        if (current_sum - k) in prefix_counts:#находим что была левая граница, а то есть и подотрезок удовлетворяющий условие 
            count += prefix_counts[current_sum - k]
        
        # Обновляем количество текущей суммы
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1            
    print(count)
count_pairs_nomer()

            # 5 17
            # 17 7 10 7 10
            # 17 24 34 41 51

#C. Туризм
#будем решать сделав 2 массива преф сумм, один слева направо, другой справа налево, далее высчитываем сумму исходя из входящего запроса
def calculation_highest_highway(): 
    # Читаем количество точек
    n = int(input())
    y_coords = []#сохраняем кординаты высоты

    # Сохраняем только y-координаты
    for _ in range(n):
        x, y = map(int, input().split())#сохраняем кор высоты в массив
        y_coords.append(y)
    
    up_forward = [0] * n #создание преф сумм слева направо
    for i in range(1, n): #от 1 до длины массива
        if y_coords[i] > y_coords[i - 1]: #если текущее выше предыдущего
            up_forward[i] = up_forward[i - 1] + (y_coords[i] - y_coords[i - 1])#то текущая сумма равна пред + разница между текущим y и пред
        else:
            up_forward[i] = up_forward[i - 1]#иначе текущая сумма равна предыдущей(если число меньше)
            
    up_backward = [0] * n #создание преф сумм справа налево
    for i in range(n - 2, -1, -1):# обратный цикл с отступом на 1 элемент от конца, тк первый 0
        if y_coords[i] > y_coords[i + 1]:#если текущая больше пред
            up_backward[i] = up_backward[i + 1] + (y_coords[i] - y_coords[i + 1])#то текущая сумма равна пред + разница двух элементов
        else:
            up_backward[i] = up_backward[i + 1]#иначе просто пред сумме
    
    m = int(input())#вводим трассы

    for _ in range(m):#цикл по трассам
        start, end = map(int, input().split())# начало и конец трасс(вершин)
        start -= 1  # переводим в 0-индексацию 
        end -= 1

        if start < end:#если конец больше начала то считаем слева направо
            result = up_forward[end] - up_forward[start]#сумму с конца отнимаем с суммой начала с первого массива
        elif start > end:#если старт больше конца то справа налево
            result = up_backward[end] - up_backward[start]#также конец - старт только сдругого массива
        else:
            result = 0

        print(result)
calculation_highest_highway()

# D. Город Че
#тк массив отсортирован то мы можем обойтись только двумя указателями, проверяя больше ли сумма чем видимость 


def counting_number_ways(): 
    n, r = list(map(int, input().split()))#считываем длину и видимость
    distances = list(map(int, input().split()))#массив расстояний
    
    count = 0 #счетчик подходящих интервалов
    right = 0#правый указатель
    for left in range(n): #левый указатель по длине массива
        while right < n and distances[left] + distances[right] <= r: #пока правый указатель не вышел за предел
            # и дистанции между указателями(интервал) меньше чем видимость 
            right += 1# мы двигаем правый указатель
            #как только дойдем до того что сумма на интервале станет больше видимости выйдем из цикла
        count += n - right # в счетчик добавим "элемент" от длины масива до правого указателя
        #тк все элементы правее чем правый указатель тоже подойдут, тк там сумма будет тоже больше чем видимость б
    print(count)#выводим счетчик
    
counting_number_ways()
        
