class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # must have the same length 
        # must have the same characters 

        if len(s) != len(t):
            return False 

        # create hashtable to hold chars 
        count_s = {}
        count_t = {}

        for letter in s:
            if letter in count_s:
                count_s[letter] += 1
            else:
                count_s[letter] = 1 
                
        for letter in t:
            if letter in count_t:
                count_t[letter] += 1 
            else:
                count_t[letter] = 1

        if count_s == count_t:
            return True 
        else:
            return False
        




