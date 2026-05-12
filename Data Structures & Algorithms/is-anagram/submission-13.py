class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        count = [0] * 26 

        for letter in s:
            count[ord(letter)-ord('a')] += 1

        for letter in t:
            count[ord(letter)-ord('a')] -= 1

    # only want to return True if all values are 0
        for val in count:
            if val != 0:
                return False

        return True 



