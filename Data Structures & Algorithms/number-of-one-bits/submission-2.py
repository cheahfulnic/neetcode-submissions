class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n & 1
            n >>= 1

        return count

        # Brian Kernighan’s algorithm
        # count = 0
        # while n:
        #     n &= (n - 1)
        #     count += 1
        # return count