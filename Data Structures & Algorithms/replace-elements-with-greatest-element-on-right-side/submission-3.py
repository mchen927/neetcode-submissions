class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNumber = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = maxNumber
            if temp > maxNumber:
                maxNumber = temp
        return arr







