#Contains Duplicate
from typing import List


class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums): #если длина списка больше чем длина множества от этоот списка, значит там есть дублированные жлементы
            return True
        return False
        
    
# Intersection of Two arrays 

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)# делаем 2 множества из списков
        set_nums2 = set(nums2)
        ans = []
        for i in set_nums1: #если элемент одного есть в другом, то это пересечение записываем в ответ
            if i in set_nums2:
                ans.append(i)
        return ans
# class Solution: альтернативный вариант используя оператор пересечения, не писав вручную
#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         return list(set(nums1) & set(nums2)) 


#Happy number
#здесь множество играет роль записи встречающихся чисел, чтобы не делать это через списки
class Solution3:
    def isHappy(self, n: int) -> bool:
        seen = set() #создаем множество для проверки, встречалось ли число ранее
        while n != 1: #делаем цикл, пока не получим единицу(счастливое число)
            if n in seen: #если n встречалось, то мы в бесконечном цикле, выходим из него
                return False
            seen.add(n)#перед преобразованием добавляем число в множество
            n = sum(int(digit) ** 2 for digit in str(n))# проверяем сумму квадратов чисел числа
        return True
    
#Longest palindrome 

class Solution:
    def longestPalindrome(self, s: str) -> int:
        set_char = set() #определяем множество для подчета вхождений символов строки
        length_palindrome = 0#начальная длина нашего палиндрома
        
        for char in s: #по всем символам в строке
            if char in set_char: #если уже есть в множестве = получается пара, которую можно разместить слева и справа 
                set_char.remove(char) #удаляем этот символ из множества
                length_palindrome += 2 #добавляем к длине палиндрома 2, тк мы взяли пару
            else: 
                set_char.add(char) #если символа нет в множестве(встрет 1 раз), то добавляем его
                
        if set_char: #если в конце множество осталось не пустое(то есть элементов нечетное количество), то мы берем его в качестве середины палиндрома
            length_palindrome += 1 #к длине палиндрома +1
            
        return length_palindrome
    
#Set Mismatch 

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_set = set()#создаем пустое множество
        duplicate = -1#начальное значение дубликата
        miss = -1 #начальное значение потерянного элемента
        
        for i in nums: #по входящему списку(множеству)
            if i in num_set: #если элемент уже есть в множестве, то это дубликат
                duplicate = i
            num_set.add(i)#иначе добавляем эоемент в множество        
        
        for j in range(1, len(nums) + 1): #цикл от 1 до n(длины входящего массива)
            if j not in num_set:#если элемента нет в множество, то это потерянный символ
                miss = j#обозначаем его 
                break#выходим с цикла
        
        return [duplicate, miss]#возвращаем список