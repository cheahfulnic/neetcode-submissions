class Solution:
    def countBits(self, n: int) -> List[int]:
        # runtime nlogn, space n
        # output = [0]

        # def getCount(n):
        #     count = 0
        #     while n:
        #         n &= (n - 1)
        #         count += 1
        #     return count

        # for i in range(1, n + 1):
        #     output += [getCount(i)]
        
        # return output

        output = [0] * (n + 1)

        for i in range (1, n+1):
            output[i] = output[i & (i - 1)] + 1

        return output