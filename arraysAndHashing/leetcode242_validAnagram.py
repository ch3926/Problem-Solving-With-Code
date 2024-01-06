# Jan 05, 2024 - Solution 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bank = {}

        if len(s) != len(t):
            return False

        # place all letters and counts into dictionary bank
        for letter in s:
            if letter in bank:
                bank[letter] += 1
            else:
                bank[letter] = 1
        
        # loop through all letters in t and check if they are found in bank
        for letter in t:
            if letter not in bank:
                return False
            if letter in bank:
                if bank[letter] == 0:
                    return False
                else:
                    bank[letter] -= 1
        
        return True


# Jan 05, 2024 - Solution 2 - Based off Neetcode
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCounts = {}
        tCounts = {}
        
        for i in range(len(s)):
            # create a new key,val pair or add one to an existing one in sCounts
            sCounts[s[i]] = 1 + sCounts.get(s[i],0)
            tCounts[t[i]] = 1 + tCounts.get(t[i], 0)

        return sCounts == tCounts

