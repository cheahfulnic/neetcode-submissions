class Solution:
    def isValid(self, s: str) -> bool:
        h = {}
        h[')'] = '('
        h['}'] = '{'
        h[']'] = '['
        stack = []
        for char in s:
            if char in h:
                if not stack:
                    return False
                else:
                    if stack.pop() == h.get(char):
                        continue
                    else:
                        return False
            else:
                stack.append(char)
        return not stack
            