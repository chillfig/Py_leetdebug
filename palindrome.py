class Solution:    
    num = None
    answer = None

    def __init__(self, x) -> answer:
        self.num = x
        self.answer = self.isPalindrome(self.num)
        self.print_attempt()

    def print_attempt(self):
        print(self.answer)

    # 9: Palindrome Number
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        reverse = len(num) - 1
        if len(num) <= 1: return True

        for i in range(len(num) // 2):
            if num[i] !=  num[reverse]:
                return False
            reverse = reverse - 1
        return True

example1 = Solution(121)
example2 = Solution(-121)
example3 = Solution(10)