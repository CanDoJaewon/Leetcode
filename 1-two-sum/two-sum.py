class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, n in enumerate(nums):
            # 1. Make a variable to find matching index
            diff = target - n
            # 2. if it found in numMap, it means we found pair. Return their index
            if diff in numMap:
                return [numMap[diff], i]

            # 3. If it's not found in numMap, store the current number in numMap.
            numMap[n] = i
