class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for _ in range(32):
            shifted = n & 1
            n >>= 1
            reverse <<= 1
            reverse |= shifted
        return reverse