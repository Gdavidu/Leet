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
        # against an undercased s. **HEXADECIMAL OR ASCII CODES
        # 2nd Pass:
class Solution:
        def isPalindrome(self, s: str) -> bool:
        # Seems like a pointer problem, was thinking of just inverting the string
        # but it seems like itd be more efficient to compare respective indices 
        # if im cycling thru the swing to invert it.
        # Create a beginning and end pointer and set the loop conmditional to end once both pointers
        # ideally == at the middle index
        # Didnt read about alphanumerics...
            undercase = s.lower()
            filteredS= ''
            for i in range(len(s)):
                if hex(ord('a')) <= hex(ord(undercase[i])) and hex(ord('z')) >= hex(ord(undercase[i])):
                    filteredS += undercase[i]
            start = 0
            end = len(filteredS)-1
            print(filteredS)
            print(start, end)
            # print(filteredS, filteredS[start], filteredS[end])
            while start < end:
                if filteredS[start] != filteredS[end]:
                # print('hit', s[start], s[end])
                    return False
                start +=1
                end -=1
            return True
# Notes: Seems like hexadecimal codes work which is strange because Im pretty sure its
# just labels and identifies each character w a certain amt of 0s?? Ascii might be betetr 
# and might just try that bc apparently they were not joshing around when instructions 
# said alphanumeric bc i really didnt even consider numeric bc who the hell cares about 
# palindromes w numbers. I gotta pick up tmrw tho its late as hell

# New Approach: filter function w isalnum() then join and compare the list and the reversed listclass Solution:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = list(filter(lambda char: char.isalnum(), s.lower()))
        # backwards = cleaned.reverse()
        # print(backwards)
        # print(cleaned)
        if cleaned[::-1] == cleaned:
            return True
        return False
# Notes: Before looking at the optimized solution I think Im at O(logn) bc Im filtering and 
# depending on how many elements I filter, it could be high in time complexity. I think space complexity
# is fine; only two new lists stored in memory.
# Conceptually, forgot how to filter and do lambda functions. Also .reverse() changes the list but 
# returns none for some dumb reason - apparently to signify they change the original list and to prevent
# unnecessary copies of the list.

# Group Anagrams:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
# Notes: Subpar sorting O(m*logn) time complexity, m being the # of strings. The idea is that ur using the sorted string as a key in the hashmap
# but you are appending the original string only if the sorted string is matching the key. The purpose of the join is to make sure that there is
# at least an empty string being added to a list and this covers the edge case of if strs only contains an empty string.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hashmaps of each word would be the best way to determines anagrms
        # but turning every word into a hashmap would eat too much space
        # I remember the solution to this was something along the lines of 
        # creating a 26 length list of 0s and then you take the ord value
        # of each char, subtract it by the ord val of a to normalize it.
        # What a solution. Each list would be like a spectrum that only
        # matches a plaindrome of itself. SO, Id need to loop the original string list and
        # make a list of 26 0s? Add a word to a list in a list if this list of 26 doesnt match any prev
        # But that would mean I need to store the previous 26 0 lists and how would I know
        res = defaultdict(list)
        
        for s in strs:
            count = [0]*26
            for char in s:
                count[ord(char) - ord('a')] += 1
            res[tuple(count)].append(s)
        return res.values()
# Notes: Real solution that creates a unique list of 26 0s, with each index representing a letter in the 26 possible letters in the alphabet.
# Taking the ascii values of each char and subtracting that by the ascii value of a, maps each letter to its correct index in the list of 0s
# Honestly a beautiful solution but it requires knowing so many niche things, such as that a list of 0s could be used to represent placement 
# in the alphabet, the [0]*26 that would create a list of 26 0s inside it, the fact that you cant use a list as a key in a hashmap so you turn it
# into a tuple first, and the defaultdict that can encompass all elements into a list. Crazy. Gotta come look at this problem more times as I go

# Top K Most Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
# Notes: Need to look over this a third time because conceptually I can tell whats going on , looking at the solution but the question itself
# was hard to discern and I wasnt sure what implications were potential edge cases or helpers. 

# Encode and Decode Strings
class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res