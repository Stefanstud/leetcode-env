"""
A **transformation sequence** from word `beginWord` to word `endWord` using a
dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... ->
sk` such that:

  * Every adjacent pair of words differs by a single letter.
  * Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
  * `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`,
return _all the **shortest transformation sequences** from_ `beginWord` _to_
`endWord` _, or an empty list if no such sequence exists. Each sequence should
be returned as a list of the words_`[beginWord, s1, s2, ..., sk]`.
"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        $$$
