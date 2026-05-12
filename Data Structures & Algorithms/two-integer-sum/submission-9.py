class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        KeyNotes:
            implement hashmap to store key, value pairs 
            {3:0}
            {4:1}
            {5:2}
            {6:3}

            complement = target - num 

            check if the complement value is in the hashmap 
            if complement value is in the hashmap return the index and key as an array

            if not continue searching
        """

        hashmap = {}

        for i in range(len(nums)): 
            complement = target - nums[i]
            
            if complement in hashmap:
                return [hashmap[complement], i]
            else:
                hashmap[nums[i]] = i


        