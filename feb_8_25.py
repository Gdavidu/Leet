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