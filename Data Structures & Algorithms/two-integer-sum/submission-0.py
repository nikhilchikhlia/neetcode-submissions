class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumNums = 0
        returnArray = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                sumNums = nums[i] + nums[j]
                if (sumNums == target):
                    returnArray.append(i)
                    returnArray.append(j)
                    return returnArray
