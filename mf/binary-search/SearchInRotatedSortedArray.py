# Problem Name: Search in Rotated Sorted Array
# Platform: Leetcode
# Problem Source: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Difficulty: Medium

# Topic: Binary Search
# Complexity: O(log n)

class Solution:
    def search(self, nums: list[int], target: int) -> int:

        # binary search for rotated lists
        def search_in_rotated_list(arr, target):

            low, high = 0, len(arr) - 1
            while low <= high:    
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid

                if arr[low] <= arr[mid]:
                    if arr[low] <= target < arr[mid]:
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if arr[mid] < target <= arr[high]:
                        low = mid + 1
                    else:
                        high = mid - 1
            return -1
        
        return search_in_rotated_list(nums, target)

