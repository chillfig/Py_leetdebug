class Solution:    
    inputString = None
    answer = None

    def __init__(self, inputString) -> answer:
        self.inputString = inputString
        self.answer = self.reverseString(self.inputString)
        self.print_attempt()

    def print_attempt(self):
        print(self.answer)

    # reverseString:
    def reverseString(self, s: str):
        if s == "":
            return ""
        else:
            return (self.reverseString(s[1:])) + s[0]

example1 = Solution("four")
example2 = Solution("racecar")