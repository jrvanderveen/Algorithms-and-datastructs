from collections import defaultdict


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        sumResultDict = defaultdict(int)
        for a in A:
            for b in B:
                sumResultDict[a+b] += 1

        count = 0
        for c in C:
            for d in D:
                count += sumResultDict[-1*(c+d)]

        return count


try:
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    expected = 2
    result = Solution().fourSumCount(A, B, C, D)
    assert result == expected
    print("Passed with expected result: ", expected)
except AssertionError:
    print("Testcast: ", A, B, C, D, " failed")
    print("Expected: ", expected)
    print("Output: ", result)
