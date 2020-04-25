'''
start 2 stacks
iterate through string
add character if not #
pop if #
'''

class Solution:
    def backspaceCompare(self, S, T):
        S_stack = []
        for char in S:
            if char == '#' and S_stack:
                S_stack.pop()
            elif char != '#':
                S_stack.append(char)

        T_stack = []
        for char in S:
            if char == '#' and T_stack:
                T_stack.pop()
            elif char != '#':
                T_stack.append(char)

        return ''.join(S_stack) == ''.join(T_stack)

solution = Solution()
print(solution.backspaceCompare(S = "ab##", T = "c#d#"))