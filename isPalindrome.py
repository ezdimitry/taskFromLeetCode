class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        return str_x == str_x[::-1]


sol = Solution()

x = 121
print(sol.isPalindrome(x))