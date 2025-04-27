class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        res = []

        def backtrack(sub="", i=0):

            if (len(sub) == len(s)):
                return res.append(sub)
            if s[i].isalpha():
                backtrack(sub + s[i].swapcase(), i + 1)
            backtrack(sub + s[i], i + 1)

        backtrack()
        return res



