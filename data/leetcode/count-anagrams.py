"""
You are given a string `s` containing one or more words. Every consecutive pair of words is separated by a single space `' '`.

A string `t` is an **anagram** of string `s` if the `ith` word of `t` is a **permutation** of the `ith` word of `s`.

* For example, `"acb dfe"` is an anagram of `"abc def"`, but `"def cab"` and `"adc bef"` are not.

Return *the number of **distinct anagrams** of* `s`. Since the answer may be very large, return it **modulo** `109 + 7`.
"""
class Solution:
    def countAnagrams(self, s: str) -> int:
        $$$