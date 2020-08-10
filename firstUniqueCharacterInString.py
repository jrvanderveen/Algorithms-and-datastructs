

class Solution(object):
    def firstUniqChar(self, s):
        charSet = set()
        charDict = dict()
        for index, c in enumerate(s):
            if c not in charSet:
                charSet.add(c)
                charDict[c] = index
            else:
                if c in charDict:
                    del charDict[c]
        if len(charDict) == 0:
            return -1
        else:
            return charDict[sorted(charDict, key=lambda key: charDict[key])[0]]


try:
    testCase = "leetcode"
    expected = 0
    result = Solution().firstUniqChar(testCase)
    assert result == expected
    print("Passed with expected result: ", expected)
except AssertionError:
    print("Testcast: ", testCase, " failed")
    print("Expected: ", expected)
    print("Output: ", result)

try:
    testCase = "loveleetcode"
    expected = 2
    result = Solution().firstUniqChar(testCase)
    assert result == expected
    print("Passed with expected result: ", expected)
except AssertionError:
    print("Testcast: ", testCase, " failed")
    print("Expected: ", expected)
    print("Output: ", result)
