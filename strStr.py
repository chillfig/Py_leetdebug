class Solution:    
    haystack = None
    needle = None
    answer = None

    def __init__(self, haystack, needle) -> answer:
        self.haystack = haystack
        self.needle = needle
        self.answer = self.strStr(self.haystack, self.needle)
        self.print_attempt()

    def print_attempt(self):
        print(self.answer)

    # fill this in
    def strStr(self, haystack: str, needle: str) -> int:
        # case that needle is an empty string
        if len(needle) == 0:
            return 0

        # iterate by all character indices in haystack
        for i in range(len(haystack)):
            # match the indices from current index to the length of needle
            if haystack[i:i+len(needle)] == needle:
                # is matched, then return the current index
                return i
        # no complete match found, return failure indicator 
        return -1

example1 = Solution("mississippi","ssipp")
example2 = Solution("aaa","aaaa")
example3 = Solution("aaaaa","bba")

# EASY SOLUTION BY USING INDEX METHOD
# # case that needle is an empty string
# if len(needle) == 0: return 0

# # case that needle is in haystack
# elif needle in haystack:
#     return haystack.index(needle)

# # nothing mathes just return -1
# return -1