# Contains Dup
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         noDupes = set(nums)
         if len(noDupes) == len(nums):
              return False
         else:
              return True
         
# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sHash, tHash = {},{}
        for i in range(len(s)):
            sHash[s[i]] = sHash.get(s[i], 0) + 1
            tHash[t[i]] = tHash.get(t[i], 0) + 1
        return sHash == tHash
# Notes: Good reminder that range is inclusive to start and exclusive to the end value
# Had to remember an easy base case that an anagram is out of the picture if the words have diff lengths,
# just a good reminder to locate edge and base cases to knock out first or have logic covering them thruout code
# Cool double initialization tech by just comma separating variable names and values respectively
# Was a little shaky with the logic and syntax of checking the set for a .get value, defaulting it to 0 otherwise, and 
# just generally adding 1. I reverse engineered it in my brain though and the logic is sound
# Efficient little boolean outcome for the return looks very clean.

# Two Sum:
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
# Return the answer with the smaller index first.

# Notes going in: Seems like a pointer problem, will definitely need a loop to compare multiple values.
# Definitely a review problem but a little shaky in memory. The examples all look like sorted lists,
# Im just going to assume sorted and see if test cases pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        while start < end:
            fixedTarget = abs(target)
            sum = abs(nums[start] + nums[end])
            if sum == fixedTarget:
                return [start,end]
            elif sum > fixedTarget:
                end-=1
            elif sum < fixedTarget:
                start+=1
# Break Notes: Even brute force not working for negative numbers, im gonna sleep on it
# Second Pass, missing something but close:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            hit = target-nums[i]
            if (hit) in nums:
                if nums.index(hit) == i:
                    return [i, nums.index(hit,i+1)]
                return [i, nums.index(hit)]
# Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # Stores {value: index}
        
        for i, num in enumerate(nums):
            hit = target - num
            if hit in num_dict:  # Check if the complement exists
                return [num_dict[hit], i]
            num_dict[num] = i  # Store the number with its index
# Notes: Got caught up on the possibility of indexing for the matching value. Didn't occur to me
# to even hashmap because I thought duplicates would mess up indexing. The solution is clean logic to me 
# tho because its using the index (a unique calue) as a key, nvm the value is a key. 

# Group Anagram
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())

# Valid Palindrome
# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Seems like a pointer problem, was thinking of just inverting the string
        # but it seems like itd be more efficient to compare respective indices 
        # if im cycling thru the swing to invert it.
        # Create a beginning and end pointer and set the loop conmditional to end once both pointers
        # ideally == at the middle index
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] != s[end]:
                print('hit', s[start], s[end])
                return False
            start +=1
            end -=1
        return True
        # First Attempt , did not properly read and now realize I need to filter out non-alphanumerical
        # characters. Thinking of just finding out which hexacodes are the alphanumerics and checking that
        # against an undercased s.