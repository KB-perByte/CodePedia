'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
'''

class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for i in S:
                if i != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)
