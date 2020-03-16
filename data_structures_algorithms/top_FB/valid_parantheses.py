class Solution:
    def isValid(self, s: str) -> bool:
        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        m = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in m.keys():  # closing braket
                top = stack.pop() if stack else "#"  # Otherwise assign a dummy value of '#'
                if m[ch] != top:  # check if the close match with open
                    return False
            else:
                # opening bracket
                stack.append(ch)

        return not stack