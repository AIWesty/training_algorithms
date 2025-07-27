# Линейный поиск - способ поиска, когда перебираются все элементы
# сложность линейного поиска O(n)
# обычно ищут наиболее подходящий элемент

#мое решение 1 задачи 
def positive_number1(x, n) -> int | None:
    index_insert = 0 
    for i in n: 
        if i == x and index_insert == 0: 
            index_insert += 1
            return i
    if index_insert == 0: 
        return -1 

print(positive_number1(4, [12, 3, 5, 3, 6,  24, 66,  1123, 557, 887]))

#решение из видео 

def positive_number2(seq, x): 
    ans = -1 
    for i in range(len(seq)): 
        if seq[i] == x and ans == -1: 
            ans = i
            return ans

print(positive_number2([12, 3, 5, 3, 6, 4, 24, 66, 4, 1123, 557, 887], 4))


# мое решение 2 задачи 

def last_pos_number(seq, x) -> int: 
    ans = -1
    for i in range(len(seq) -1, -1, -1):
        if seq[i] == x and ans == -1: 
            ans = i
    return ans

print(last_pos_number([12, 3, 5, 3, 6, 4, 24, 66, 4, 1123, 557, 887], 4))

#решение из видео 

def last_pos_number2(seq, x): 
    ans = -1 
    for i in range(len(seq)): 
        if seq[i] == x: 
            ans = i
    return ans


#мое решение 3 задачи 
def max_num(seq) -> int: 
    max_num = 0 # при наличии 1 элемента код не сработает, тк элемент может быть меньше 0 
    for i in seq: 
        if i > max_num: 
            max_num += i
    return max_num

#решение из видео 

def max_num1(seq): 
    max_num = seq[0] # берем первый элемент и сравниваем со следующими
    for i in range(len(seq)):
        if seq[i] > max_num: 
            max_num += seq[i]
    return max_num
# в задачах поиска минимума и максимума обычно принято брать в переменную ответа первый элемент

#более правильное решение на мой взгляд, не используя индексы а просто проходясь по последовательности
#тк нас просят найти самый большой элемент
def find_max_num(seq): 
    ans = seq[0]
    for i in seq: #можно начать идти с 1 элемента
        if i > ans: 
            ans = i #для строк в других языках можно запоминать индексы
    return ans

#задача 4 мое решение

def two_max_number(seq): 
    first_elem = seq[0]
    sec_elem = seq[1]
    max1 = max([first_elem, sec_elem])
    max2 = min([first_elem, sec_elem])
    for i in range(2, len(seq)): 
        if seq[i] > max1: 
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2 and seq[i] < max1: 
            max2 = seq[i]
    return (max1, max2)

#решение из видоса

def two_max_num(seq): 
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range(len(seq)): 
        if seq[i] > max1: 
            max2 = max1 
            max1 = seq[i]
        elif seq[i] > max2: 
            max2 = seq[i]
    return (max1, max2)

#5 задача мое решение 

def minimum_positive_number(seq): #не решил, не понимаю что взять за первое число минимума
    if len(seq) > 0: 
        ans = 0 #логика с начальном значением верная, но не правильно реализована 
        for i in range(len(seq)): 
            if seq[i] % 2 == 0 and ans == 0:
                ans = seq[i]
            elif seq[i] % 2 == 0 and seq[i] < ans: 
                ans = seq[i]
            else: 
                ans = -1 #здесь элсе скидывает значение при каждом нечетном числе что неверно
    return ans 
        

# решение из видоса 

def min_pos_num(seq): 
    ans = -1  # считаем что подходящего элемента нет
    for i in range(len(seq)): 
        if seq[i] % 2 == 0 and (ans == - 1 or seq[i] < ans): #если число четное и оно не встречалось ИЛИ оно меньше предыдущего минимума
            ans = seq[i]
    return ans
#также можем вместо -1 поставить flag = False и потом проверять вместо ans == -1
    
    

#6 задача мое решение 
def short_word(seq): 
    ans = [] #список для коротких слов
    min_symbols = len(seq[0]) #первый элемент самый короткий 
    for i in seq: #первый проход для количества букв в самом коротком слове
        if len(i) < min_symbols:
            min_symbols = len(i)
    for j in seq: #второй проход длядобавления всех коротких слов
        if len(j) == min_symbols: 
            ans.append(j)
    return ', '.join(ans)


#решение из видео 

def shortword(seq): 
    minlen = len(seq[0])
    for word in seq: 
        if len(word) < minlen:
            minlen = len(word)
    ans = ''
    for word in seq: 
        if len(word) == minlen: 
            ans += word + ' ' 
    return ans

#задача с собеса мое решение 
def rle1(seq): 
    counter = 0 
    ans = []
    if len(seq) > 0:
        for i in range(1, len(seq)): 
            if seq[i] == seq[i - 1]:
                counter += 1  #пытаюсь подсчитать количество букв
            else: 
                counter = 0
    else: 
        raise ValueError

#решение с видоса

def rle(seq): 
    def pack(seq, cnt): # принимаем последний символ и количество вхождений в последовательность
        if cnt > 1: #если встречался больше раза то обьединяем символ и колество
            return seq + str(cnt)
        return seq
    lastsym = seq[0] # последний символ(предыдущий)
    lastpos = 0 #последняя позиция последовательности элементов
    ans = []
    for i in range(len(seq)):
        if seq[i] != lastsym: #если текущий не равен предыдущему
            ans.append(pack(lastsym, i - lastpos)) #добавляем его исходя из количество вхождений
            lastpos = i #перезаписываем позицию - новая последовательность будет начинаться на символе не схожим с пред, то есть i
            lastsym = seq[i] #последний символ становится i
    ans.append(pack(seq[lastpos], len(seq) - lastpos))#добавляем последний символ
    return ''.join(ans)