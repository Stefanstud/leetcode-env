class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:
    i = len(s) - 1
    j = len(t) - 1

    while i >= 0 or j >= 0:
      backspace = 0
      while i >= 0 and (s[i] == '#' or backspace > 0):
        backspace += 1 if s[i] == '#' else -1
        i -= 1
      backspace = 0
      while j >= 0 and (t[j] == '#' or backspace > 0):
        backspace += 1 if t[j] == '#' else -1
        j -= 1
      if i >= 0 and j >= 0 and s[i] != t[j] or \
          i < 0 and j >= 0 and s[j] != '#' or \
              j < 0 and i >= 0 and s[i] != '#':
        return False
      i -= 1
      j -= 1

    return True
