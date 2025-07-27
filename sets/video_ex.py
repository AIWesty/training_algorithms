#свое мультимножество (множество в которое элемент может входить несколько раз), тк при проверка мы не проверяем наличия элемента
set_size = 10
myset = [[] for _ in range(10)]#генератор списков(нашего множества)
def add(x): 
    #if not in myset[x % set_size]:
    myset[x % set_size].append(x)#добавление элемента в множество
    #else return
    
def find(x): 
    for now in myset[x % set_size]: #поиск элемента в множестве, идем по списку(по тому, который получился из хеша)
        if now == x: 
            return True
    return False

def delete(x):
    xlist = myset[x % set_size]#определяем номер списка
    for now in range(len(xlist)): #ищем удаляемый элемент
        if now == xlist[x]:
            xlist[now], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[now]#меняем найденный элемент с последним
            xlist.pop()#удаляем последний элемент 
            return 
        

#задача 1 с последовательностью

def find_two_adders(n, x):
    myset = set(n)
    for i in myset:
        if x - i in myset:
            return (i, x - i)
    return (0, 0)
#можно решить через такой же проход по списку, и добавление в множество в конце, но разницы по сути нет

#задача 2 hешение за O(N * K **2 + M) 
def inner_miss_elem(dictionary, text):
    goodword = set(dictionary)#делаем множество из нашего словаря
    for i in dictionary():#пробегаемся по словарю
        for delpos in range(len(i)):#по длине слова в словаре
            goodword.add([i[:delpos] + i[delpos + 1:]])#в множество добавляем вариант слова с удаленным символом
    ans = [] 
    for word in text: 
        ans.append(word in goodword)#проверяем есть ли слово в словаре, булевое значение
    return ans
