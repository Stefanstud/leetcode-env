class Solution {
 public:
  bool backspaceCompare(string s, string t) {
    int i = s.length() - 1;  // s's index
    int j = t.length() - 1;  // t's index

    while (true) {
      // Delete chars of s if needed
      int back = 0;
      while (i >= 0 && (s[i] == '#' || back > 0)) {
        back += s[i] == '#' ? 1 : -1;
        --i;
      }
      // Delete chars of t if needed
      back = 0;
      while (j >= 0 && (t[j] == '#' || back > 0)) {
        back += t[j] == '#' ? 1 : -1;
        --j;
      }
      if (i >= 0 && j >= 0 && s[i] == t[j]) {
        --i;
        --j;
      } else {
        break;
      }
    }

    return i == -1 && j == -1;
  }
};
