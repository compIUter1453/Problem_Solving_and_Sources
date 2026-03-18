# Problem Name: Median of Two Sorted Arrays
# Platform: Leetcode
# Problem Source: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Difficulty: Medium

# Topic: Data Structures
# Complexity: O(n + m)

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        m = len(nums1)
        n = len(nums2)
        res = []

        idx1=0
        idx2=0
        for _ in range(m + n):
            if idx1 < m and (idx2 >= n or nums1[idx1] < nums2[idx2]):
                res.append(nums1[idx1])
                idx1 += 1
            elif idx2 < n:
                res.append(nums2[idx2])
                idx2 += 1
            else:
                break
        
        if (n+m) % 2 == 1:
            med = res[int((n+m)/2)]
        else:
            med = (res[int((n+m)/2-1)]*1.0 + res[int((n+m)/2)]*1.0) / 2.0

        return med
