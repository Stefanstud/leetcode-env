"""
You are given a string `word` and an array of strings `forbidden`.

A string is called **valid** if none of its substrings are present in `forbidden`.

Return *the length of the **longest valid substring** of the string* `word`.

A **substring** is a contiguous sequence of characters in a string, possibly empty.
"""
class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        $$$