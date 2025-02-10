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