from collections import Counter


class Solution():
    def longestSubstring(self, s, k):
        if s == "":
            return 0
        char, count = Counter(s).most_common()[-1]
        if count >= k:
            return len(s)
        maxLen = 0
        for sub in s.split(char):
            maxLen = max(maxLen, self.longestSubstring(sub, k))
        return maxLen


try:
    testCase = "aabbc"
    expected = 4
    result = Solution().longestSubstring(testCase, 2)
    assert result == expected
    print("Passed with expected result: ", expected)
except AssertionError:
    print("Testcast: ", testCase, " failed")
    print("Expected: ", expected)
    print("Output: ", result)
