#Two sum 
#перво что пришло в голову решение за O(n ** 2) создав словарь(цикл) и потом по нему пройтись 
#для масива более легкое решение 

from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}#создаем пустой словарь 
        for i, num in enumerate(nums): #проходим по индексам и элементам входящего списка
            if not target - num in dict_nums: #если искомое число - текущее не в словаре 
                dict_nums[num] = i#то просто добавляем элемент
            else: 
                return [dict_nums[target - num], i]#выводим индексы подходящих элементов
            
#First Unique Character in a String 

#O(N) time, O(1) space, можнооптимизировать, но сложно 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_of_string = {}#создаем пустой словарь
        for i in s: #бежим по строке 
            if i not in dict_of_string: #если символа нет в словаре
                dict_of_string[i] = 0 #по его ключу инициализируем ноль
            dict_of_string[i] += 1 #если есть(в любом случае) добавляем 1
        for j in range(len(s)): #пробегаемся по строке еще раз 
            if dict_of_string[s[j]] == 1: #если находим элемент который встречался всего раз 
                return j#то выводим его 
        return -1
    
#Contains Duplicate 2
#решение за O(n) по времени, и O(n)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict_index = {} #Будем хранить {число: его последний индекс}
        for i, num in enumerate(nums): # идем по индексам и элементам
            if num in dict_index and abs(i - dict_index[num]) <= k: #если мы уже встречали элемент(то есть текущему элементу был раньше подходящий)
                return True 
            dict_index[num] = i #обновляем последний индекс этого элемента, это сделано чтобы
            # при встрече новых элементов(например в списке[2, 3, 2, 2 ] - три двойки, поэтому нам могут подходить несколько индексов)
        return False
    
    
    
    
#Intesection of Two arrays 2
#мое решение это первый массив записать в словарь и потом из пройтись по второму, если число из второго есть в словаре добавляем его в ответный масив
#такое решение было бы за O(n * m)


#решение тут O(n + m)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_of_nums1 = {}#создаем два словаря для подсчета всех вхождений
        dict_of_nums2 = {}
        for num in nums1:#считаем вхождения для обоих списков
            if num not in dict_of_nums1:
                dict_of_nums1[num] = 0
            dict_of_nums1[num] += 1
        for num in nums2: 
            if num not in dict_of_nums2:
                dict_of_nums2[num] = 0
            dict_of_nums2[num] +=1 
        
        result = []#результирующий список
        for num in dict_of_nums1: #идем по любом из словарей
            if num in dict_of_nums2: #проверяем есть ли текущий элемент в другом словаре
                result.extend(([num] * min(dict_of_nums1[num], dict_of_nums2[num])))#расширяем массив с ответом 
                #на минимальное количество текущего элемента из двух словарей
        return result
    
#можно использовать defaultdict для автоматического заполнения несуществующего ключа нулем

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        
        
        dict_of_nums1 = defaultdict(int) #автоматом заполняет нулями несущ ключи
        dict_of_nums2 = defaultdict(int)
        
        for num in nums1: 
            dict_of_nums1[num] += 1
            
        for num in nums2: 
            dict_of_nums2[num] += 1
        
        result = []#результирующий список
        for num in dict_of_nums1: #идем по любом из словарей
            if num in dict_of_nums2: #проверяем есть ли текущий элемент в другом словаре
                result.extend(([num] * min(dict_of_nums1[num], dict_of_nums2[num])))#расширяем массив с ответом 
                #на минимальное количество текущего элемента из двух словарей
        return result
    
#Group anagrams 
#O(n) time, O(n) space
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_in = {}#определеям пустой словарь
        
        for i in strs: #проходим по входящему списку
            i_sorted = ''.join(sorted(i))#делаем ключ - берем отсортированную строку
            #значения будет список с  входящими строками
            if i not in count_in: #если еще нет в словаре
                count_in[i_sorted] = [] #инициализируем пустой словарь по заготовленному ключу
            count_in[i_sorted].append(i) #добавляем текущий элемент в список
            
        return list(count_in.values())#делаем список из списков словаря
    
    
    
#Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_entry = {}#инициализация пустого словаря
        for i in nums: #проходим по поступающему списку
            if i not in count_entry:#если элемент еще не в словаре
                count_entry[i] = 0#инициализируем по ключу 0
            count_entry[i] += 1 #добавляем 1 
        sorted_count = sorted(count_entry.items(), key= lambda x: x[1], reverse=True)#сортируем подсчитанный словарь по значениям в обратном порядке
        #чтобы элементы с самым большим кол-вом вхождений были вначале
        return [item[0] for item in sorted_count[:k]]#идем по словарю до k(столько, сколько нужно вывести элементов)
        #сохраняем ключ(первый элемент, тк отсортированный словарь вида: [(key, val), (key, val), ...])
        
        
#4Sum2
#решение за O(n ** 2) time, по памяти O(N)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_counts = defaultdict(int)#создаем словарь для подсчета сумм пар из первых массивов
        
        for i in nums1: #пробегаемс по первому и второму словарю
            for j in nums2: 
                sum_counts[i + j] += 1 #помечаем 1 каждую сумму из двух словарей
        
        count = 0#счетчик подходящих
        
        for k in nums3: #проходим по оставшимся масивам
            for l in nums4: 
                s = k + l #вычисляем сумму для каждого и проверяем
                if -s in sum_counts: #если в словаре уже есть отрицательная сумма(ключ) которая дает противоположную сумму массивов 3,4  
                    count += sum_counts[-s] #добавляем каждый подходящий 
        return count
        
#Valid anagram 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = defaultdict(int) #создаем словарь для подсчета вхождений
        
        if len(s) != len(t): #если длины разные сразу вовзврат false
            return False
        
        for i in s: #пробегаемся по первой строке
            char_count[i] += 1 #считаем символы в словарь
            
        for j in t: #пробегаемся по второй строке 
            char_count[j] -= 1 #отнимаем от счетчика 1
            if char_count[j] < 0: #если он ушел в минус - слова не анограмы(во второй строке больше букв других букв)
                return False
            
        return True
                    