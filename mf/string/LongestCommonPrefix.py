# Problem Name: Longest Common Prefix
# Platform: Leetcode
# Problem Source: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy

# Topic: String
# Complexity: O(n+l)

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        prefix = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
