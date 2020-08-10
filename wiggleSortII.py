class Solution:
    def wiggleSort(self, nums):
        arr = sorted(nums)
        for i in range(1, len(nums), 2):
            nums[i] = arr.pop()
        for i in range(2, len(nums), 2):
            nums[i] = arr.pop()
        return nums


try:
    testCase = [1, 5, 1, 1, 6]
    expected = [1, 6, 1, 5, 1]
    result = Solution().wiggleSort(testCase)
    assert result == expected
    print("Passed with expected result: ", expected)
except AssertionError:
    print("Testcast: ", testCase, " failed")
    print("Expected: ", expected)
    print("Output: ", result)
