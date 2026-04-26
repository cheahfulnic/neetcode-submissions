class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = 0
        for integer in nums:
            bits ^= integer
        return bits