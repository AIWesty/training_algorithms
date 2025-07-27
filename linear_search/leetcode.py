#find minimum in Rotated Sorted Array (solved by linear)
from typing import List


class Solution1:
    def findMin(self, nums: List[int]) -> int:
        min_symbol = 0
        for i in range(len(nums)): 
            if nums[i] < min_symbol: 
                min_symbol = nums[i]
        return min_symbol


nums = list(map(int, input().split()))

#Max Consecutive Ones

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0 #максимальная последовательность единиц
        current_cons = 0 #текущая последовательность единиц
        for i in nums: 
            if i == 1:#если единици  
                current_cons += 1 #текущую увеличиваем на1 
                max_cons = max(max_cons, current_cons) #переопределяем максимум, выбираем из текущей и максимальной, для каждой новой
            else: 
                current_cons = 0#если встретили ноль обнулили текушую послед
                
        return max_cons
    
#крутое универсальное решение для любых последовательностей, а не только едининц

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        max_length = 1
        current_length = 1
        last_element = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == last_element:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1
                last_element = nums[i]
                
        return max_length if 1 in nums else 0  # Для задачи с единицами
    
# Find all numbers Disappeared in an Array 

#O(n**2)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(nums) + 1): 
            if i not in nums:
                ans.append(i)
        return ans
    
#O(n) с пометкой в массиве
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums: #проходимся по нашему списку
            index = abs(num) - 1 #получаем индекс элемента (для  массива от 1 до n)
            if nums[index] > 0: #если еще не помечен
                nums[index] *= -1 #помечаем элемент отрицательным числом
        #собираем отсутствующие числа
        result = []
        for i in range(len(nums)):#по индексам массива
            if nums[i] > 0: #если число не помечено 
                result.append(i + 1)#добавляем пропущенное число, +1 потому что от индекса
        return result
#O(n) понятное через множество 

def findDisappearedNumbers(nums):
    num_set = set(nums) #делаем из нашего списка множество, отсекая повторяющиеся элементы
    return [i for i in range(1, len(nums) + 1) if i not in num_set] #проходим по длине масива и если элемента нет в нашем множестве, то добавляем его в список

#Find all duplicates in array
#O(n)
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        new_nums = set()
        ans = []
        for i in range(len(nums)): 
            if nums[i] not in new_nums: 
                new_nums.add(nums[i])
            else: 
                ans.append(nums[i])
        return ans
    
# Valid Mountain array 

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ans = False
        mountain_index = 0
        if len(arr) >= 3:
            for i in range(1, len(arr) - 1): 
                if arr[i] > arr[i - 1] and arr[i] > arr[i + 1] and mountain_index == 0:
                    ans = True
                    mountain_index += 1
        return ans