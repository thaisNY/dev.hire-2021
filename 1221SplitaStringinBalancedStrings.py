class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        if len(s) == 1:
            return 0
        for char in s:
            if char == 'L':
                left +=1
            else:
                right += 1
            if left == right:
                ans +=1
        return ans
