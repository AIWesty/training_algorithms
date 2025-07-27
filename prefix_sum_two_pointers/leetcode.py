#Running sum of 1d Array 

#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.

#решение за O(n) по времени и памяти 
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0]] * len(nums)#сделали массив из первого символа массива, тк неивестно заранее элемент
        #и по длине масива, а не +1 как в дефолтных задачах, тк тут первый элемент не нулевой(преф сумма на первом = первому элементу)
        for i in range(1, len(nums)): #пропускаем первый эл, до длины массива
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]#заменяем в масиве на предыдущую сумму + текущее число
        return prefix_sum
    

#Range sum Query - immutable
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * len(nums) #при инициализации обьекта создаем массив преф сум
        if nums: #если он не пустой 
            self.prefix_sum[0] = nums[0]#то первая сумма равна первому элементу вход массива
            for i in range(1, len(nums)): #от первого до длины
                self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i]#текущая сумма = пред сумма + текущий элемент массива

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: #если левая граница с начала 
            return self.prefix_sum[right] # то просто возвращаем правую границу 
        else: 
            return self.prefix_sum[right] - self.prefix_sum[left - 1]#если интервал другой
        # то от правой границы вычитаем левую - 1
        #почему -1? потому что правая граница это сумма от 0 до right
        #нам нужно оставить только промежуток от left до right
        #это можно сделать вычесть из правой левую ВКЛЮЧИТЕЛЬНО, то есть откинуть сумму до левого элемента
        # поэтому - 1
        [1, 2, 3, 4, 5]
        [1, 3, 6, 10, 15]

# Maximum Average Subarray I
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefix_average = [0] * len(nums)
        prefix_average[0] = nums[0]
        for i in range(1, len(nums)): 
            prefix_average[i] = prefix_average[i - 1] + nums[i]
        #мое недоделанное решение с префиксными суммами(туда надо добавить слайдинг виндоу)

from collections import defaultdict
from shutil import move
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 1. Создаём массив префиксных сумм
        prefix = [0] * (len(nums) + 1)  # Длина на 1 больше, чтобы удобнее считать суммы
        
        # 2. Заполняем префиксные суммы:
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        
        # 3. Ищем максимальную сумму подмассива длины k
        max_sum = float('-inf')  # Начальное значение (минимально возможное)
        
        # 4. Проходимся по префиксным суммам и вычисляем суммы подмассивов длины k
        for i in range(k, len(nums) + 1):
            current_sum = prefix[i] - prefix[i - k]  
            max_sum = max(max_sum, current_sum)  # Обновляем максимум
        
        return max_sum / k #среднее значение 
    
    
#560. Subarray Sum Equals K. СУММА НА ЭТИХ ИНТЕРВАЛАХ!!!!!
#решение за O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counts = defaultdict(int)#мы делаем словарь преф сумм, ключ сумма - значение сколько раз встречалась такая сумма
        prefix_counts[0] = 1 #сумма 0 встречалась 1 раз до начала массива, грубо говоря инициализация для подмасива с нулевого элемента
        prefix_sum = 0 #счетчик текущей преф суммы
        count = 0 #итоговый счетчик подмассивов
        
        for num in nums: #по массиву
            prefix_sum += num#увеличиваем текущую преф сумму
            if (prefix_sum - k) in prefix_counts:# если число текущей суммы - k есть в словаре
                #это эквивалент prefix_sum[j](правая граница интервала) - prefix_sum[i](левая граница интервала) = k
                # то есть сумма на отрезке (i:j) = k, мы проверяем если правая - k ,то есть такая левая от которой будет подмасив с k суммой
                count += prefix_counts[prefix_sum - k] #в счетчик прибавляем количество раз сколько встречалась сумма такая
            prefix_counts[prefix_sum] += 1#добавляем по префиксной сумме +1
    
        return count 
    


# Product of Array Except Self
#лобовое решение просто пройтись по массиву и добаввлять в список произведения до i и от i 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0 
        ans = []
        for i in range(len(nums)):
            for j in range(i):
                count *= nums[j]
            for q in range(i + 1, len(nums)):
                count *= nums[q]
            ans.append(count)
        return ans

#оптимизированное решение, мы считаем два массива произведений, слева направо, и справо налево 
#произведение 2х итых, то есть befor_i[i] * after_i[i] = answe[i], а если проще то произведению элементов до стоящего числа и после 
#решение за O(n) time, O(n)space, можно по памяти за O(1), если не хранить в массиве а в переменной
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        before_i = [1] * n#массив произведений до i
        after_i = [1] * n#массив произведелний после i
        answer = [1] * n#ответ, все заполнено 1, чтобы при умножении не изменять значение 
        
        for left in range(1, n):#префиксное произведение слева направо от начала до конца
            before_i[left] = before_i[left - 1] * nums[left - 1] #
            
        for right in range(n - 2, -1, -1): #индексация с нуля, начинается с предпоследнего элемента массива
            after_i[right] = after_i[right + 1] * nums[right + 1]#
            #идем справа налево по массиву
            
        for i in range(n):#по длине всего масива
            answer[i] = before_i[i] * after_i[i]#элемент из массив ответа = элемент первго массива на элемент правого массива
        return answer

        # nums:    [1,   2,   3,   4]
        # before_i:[1,   1,   2,   6]  # Произведения всех элементов слева от i
        # after_i: [24, 12,   4,   1]  # Произведения всех элементов справа от i
        # answer:  [24, 12,   8,   6]  # before_i[i] * after_i[i] для каждого i


# 283. move Zeroes
#Самое наивное решение с созданием нового массива(копией), это посчитать кол-во нулей в массиве(удаляя их), потом просто в конец добавить такое же кол-во нулей
#это решение было бы за O(n)


#решение в два указателя 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0 #левый указатель 
        
        for j in range(len(nums)): #правый указатель по длине массива
            if nums[j] != 0: #если элемент не равен нулю
                nums[i], nums[j] = nums[j], nums[i] #то правый ненулевой меняется с левым элементамм
                i += 1 #двигаем левый указатель вправо
                
        return nums 
    
#26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:#проверка краевого случая
            return 0
        i = 0 #левый указатель
        
        for j in range(1, len(nums)):#правый указатель по длине массива
            if nums[j] != nums[i]:#если правый не равен левому, то есть мы нашли новый элемент(уникальный, тк массив сорт)
                i += 1 #то двигаем левый указатель правее
                nums[i] = nums[j]#на место левого указателя ставим элемент правого указателя
                
        return i + 1#количество уникальных элементов +1
            
#[0,1,2,3,4,2,2,3,3,4]

#344. Reverse String
#решение in-place двумя указателями, на каждой итерации двигать указатели обмениваясь значениями
#остановка на индексе деления на 2 + 1 
#O(n) time, O(1) space
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0 #левый указатель, двигаем вправо на 1 
        right = len(s) - 1#правый указатель, двигаем влево на 1, начинаем с конца строки(len(s) - 1) 
        while left < right: #пока левый указатель меньше правого(по индексу), значит они не встретились и можно продолжать цикл
            s[left], s[right] = s[right], s[left]#обмениваем значениями левый и правый указатель
            left += 1 #двигаем указатели
            right -= 1
        
# 3Sum
#решение это сортировка массива, два указателя, двигаем правый + правый(+1) от левого и ищем, если они в сумме дают 0, двигаем левый
#решени не доделано(неправильное, тк проверяем только соседние элементы, а должны искать во всем массиве) 
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            ans = []
            left = 0 
            right = 1
            while right < len(nums) - 1: 
                if nums[left] + nums[right] + nums[right + 1] == 0: 
                    ans.append([left, right, right + 1])
            right += 1
            left += 1
            return ans 

#здесь не получится решение за O(n) двумя указателями
#решение получается за O(n ** 2) time, O(n) space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#сортировка для избавления от дублирующихся элементов
        ans = []#пустой массив для ответа
        n = len(nums)#длина массива
        for i in range(n - 2): #-2 чтобы не выйти за конец последовательности, тк проверяем 3 числа
            if i > 0 and nums[i] == nums[i - 1]: #проверяем если i > 0 и текущий элемент равен предыдущему
                continue #то пропускаем итерацию, тк это дублирующийся элемент
            left = i + 1 #левый указатеь на i + 1, тк нужно 3 числа
            right = n - 1 #правый указатель на конец последовательности
            
            while left < right: #пока левый указатель не дошел до правого 
                total = nums[i] + nums[left] + nums[right]#текущая сумма 3 эл на данной итерации
                
                if total < 0: #если сумма меньше 0, двигаем левый указатель, тк массив отсортирован нам нжуен больший элемент
                    left += 1
                elif total > 0: #если больше нуля то нужен меньший элемент
                    right -= 1
                else: 
                    ans.append([nums[i], nums[left], nums[right]])#добавляем ответ
                    while left < right and nums[left] == nums[left + 1]:#два цикла для проверки дубликатов влево и вправо, чтобы мы их не брали в ответ
                        left += 1 #проверяем вправо, если след элемент такой же, то просто пропускаем его
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1#проверяем справа налево, если след элемент такой же то пропускаем его 
                    left += 1#двигаем указатели для след итерации
                    right -= 1 
        return ans
#[-1,0,1,2,-1,-4]
#[-4,-1,-1,0,1,2]
#[]

#167. Two Sum II - Input Array Is Sorted
#лобовое решение, тк массив сортирован, пробегать двумя указателями с начала и с конца,
# искать подходящий элемент,
#если сумма больше чем надо двигаем правый указатель, если иначе то левый
#решение за O(n) time, O(1) space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 #левый указатель  в начало массива
        right = len(numbers) - 1#правый в конец массива
        for _ in range(len(numbers)):#по длине масива
            if numbers[left] + numbers[right] > target: #если текущая сумма указателей больше таргета, то двигаем правый укзатель
                right -= 1
            elif numbers[left] + numbers[right] < target: #если тек сумма меньше то двигаем левый
                left += 1 
            else: 
                ans = [left + 1, right + 1]#ответ 2 индекса текущие
                break#можем прерывать цикл, тк по условию 1 ответ
        return ans
#более красивое решение 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 #левый указатель  в начало массива
        right = len(numbers) - 1#правый в конец массива
        
        while left < right: #пока не столкнулись указатели(while здесь удобнее и лаконичнее)
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1
                