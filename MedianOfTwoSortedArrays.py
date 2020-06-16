#####
# Input      : two sorted arrays on ints
# Output     : the median value of the two arrays
# Constraint : overall run time O(log (m+n)) where m = array1.len and n = array2.len
# Edge cases :
#####


'''
The median value is the middle value in a list.
For this solution we simply need to iterate through both lists in order recording the values as we go.
Since both lists are sorted we just need to keep track of an index for each list and check which value is large between both lists.
once through add the remaining items.

Now we have a single sorted list and can return the middle value if the list has an odd number of entries or (two middle values / 2) for even.
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = []
        i1 = 0
        i2 = 0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                nums.append(nums1[i1])
                i1 += 1
            else:
                nums.append(nums2[i2])
                i2 += 1

        while i1 < len(nums1):
            nums.append(nums1[i1])
            i1 += 1
        while i2 < len(nums2):
            nums.append(nums2[i2])
            i2 += 1

        # print(nums)

        if len(nums) % 2 == 0:
            # returnNum = (nums[int(len(nums)/2)] + nums[int((len(nums)/2))-1]) / 2
            # print(returnNum)
            return (nums[int(len(nums)/2)] + nums[int((len(nums)/2))-1]) / 2
        else:
            # returnNum = (nums[int(len(nums)/2)])
            # print(returnNum)
            return (nums[int(len(nums)/2)])
