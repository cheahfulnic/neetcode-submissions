class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, number in enumerate(nums):
            if target - number in h:
                return [h[target - number], i]
            h[number] = i