class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        ways_one, ways_two = 1, 2
        for _ in range(3, n + 1):
            current = ways_one + ways_two
            ways_one = ways_two
            ways_two = current

        return ways_two