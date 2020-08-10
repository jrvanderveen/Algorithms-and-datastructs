def printArray(array):

    for row in range(len(array)):
        print()
        for col in range(len(array[0])):
            print(array[row][col], " ", end="")
    print()


class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        count = 0
        for start in range(n-1, -1, -1):
            for end in range(start, n):
                # start and end must be equal
                if s[start] != s[end]:
                    dp[start][end] = 0
                # if len < 3 and start == end then found
                elif end-start+1 < 3:
                    dp[start][end] = 1
                # if len >= 3 and start == end then check if inner substring pal
                else:
                    dp[start][end] = dp[start+1][end-1]

                count += dp[start][end]
        return count


try:
    testCase = "fdsklf"
    expected = 6
    result = Solution().countSubstrings(testCase)
    assert result == expected
    print("Passed with expected result: ", expected)
except AssertionError:
    print("Testcast: ", testCase, " failed")
    print("Expected: ", expected)
    print("Output: ", result)

try:
    testCase = "abba"
    expected = 6
    result = Solution().countSubstrings(testCase)
    assert result == expected
    print("Passed with expected result: ", expected)
except AssertionError:
    print("Testcast: ", testCase, " failed")
    print("Expected: ", expected)
    print("Output: ", result)

try:
    testCase = "aaa"
    expected = 6
    result = Solution().countSubstrings(testCase)
    assert result == expected
    print("Passed with expected result: ", expected)
except AssertionError:
    print("Testcast: ", testCase, " failed")
    print("Expected: ", expected)
    print("Output: ", result)

try:
    testCase = "abc"
    expected = 3
    result = Solution().countSubstrings(testCase)
    assert result == expected
    print("Passed with expected result: ", expected)
except AssertionError:
    print("Testcast: ", testCase, " failed")
    print("Expected: ", expected)
    print("Output: ", result)
