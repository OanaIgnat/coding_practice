"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.


Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
"""
from typing import List


class Solution:

    def compare_indexes(self, ch1, ch2, order):
        if order.index(ch1) < order.index(ch2):
            return 1
        else:
            return 0

    # The words are sorted lexicographically if and only if adjacent words are.
    # This is because order is transitive: a <= b and b <= c implies a <= c.
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        for m in range(len(words) - 1):
            a = words[m]
            b = words[m + 1]
            i, j = 0, 0
            # find first difference
            found_first_diff = 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    if self.compare_indexes(a[i], b[j], order) == 0:
                        return False
                    else:
                        found_first_diff = 1
                        break

            if not found_first_diff and len(a) > len(b):
                return False

        return True

