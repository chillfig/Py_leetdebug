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
        # negative numbers are not Palindrome
        if x < 0: return False

        inputNum = x    # store original input num
        newNum = 0      # represents the reversed version

        # algorithm that populates newNum by taking the last digit off of x every iteration
        while x > 0:
            # (raise the place value of the last collected digit) + (the next last digit of x)
            newNum = (newNum * 10) + (x % 10)
            # now reduce x from the last digit you just collected
            x = x // 10
        # exit while loop when x becomes 0
        return newNum == inputNum

example1 = Solution(121)
example2 = Solution(-121)
example3 = Solution(2332)