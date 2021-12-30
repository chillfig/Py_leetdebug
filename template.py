class Solution:    
    input = None
    answer = None

    def __init__(self, input) -> answer:
        self.input = input
        self.answer = self.ourFunction(self.input)
        self.print_attempt()

    def print_attempt(self):
        print(self.answer)

    # fill this in
    def ourFunction(self, s: str):
        return s

example1 = Solution("(()[]")
example2 = Solution("{[]}")
example3 = Solution("(]")