"""
Removing max one character -> is palindrom ?
"""
class Solution:
    # O(n) time; O(n) space
    """
    Runtime: 64 ms, faster than 96.51% of Python3 online submissions for Valid Palindrome II.
    Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Valid Palindrome II.
    """

    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    tmp1 = s[:i] + s[i + 1:]
                    tmp2 = s[:j] + s[j + 1:]
                    return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]

            return True

    """
    Runtime: 152 ms, faster than 62.36% of Python3 online submissions for Valid Palindrome II.
    Memory Usage: 13.2 MB, less than 75.00% of Python3 online submissions for Valid Palindrome II.
    """

    def validPalindrome2(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            i = 0
            j = len(s) - 1
            removed = 0
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    if removed == 1:
                        removed = 2
                        break
                    i += 1
                    removed = 1
        if removed != 2:
            return True

        i = 0
        j = len(s) - 1
        removed = 0
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                if removed == 1:
                    return False
                j -= 1
                removed = 1
        return True

    """
    Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.
    
    Example 1:
    
    Input: "A man, a plan, a canal: Panama"
    Output: true
    """

    """
    Runtime: 80 ms, faster than 9.27% of Python3 online submissions for Valid Palindrome.
    Memory Usage: 13.4 MB, less than 71.43% of Python3 online submissions for Valid Palindrome.
    """
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < len(s) and j >= 0:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
            else:
                if s[i].isalnum():
                    j -= 1
                else:
                    i += 1
        return True

    """
    Runtime: 36 ms, faster than 93.54% of Python3 online submissions for Valid Palindrome.
    Memory Usage: 14 MB, less than 52.38% of Python3 online submissions for Valid Palindrome.
    """
    def isPalindrome2(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([x for x in s if x.isalnum()])
        return s == s[::-1]

