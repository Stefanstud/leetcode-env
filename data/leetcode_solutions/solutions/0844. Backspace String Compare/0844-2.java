class Solution {
  public boolean backspaceCompare(String s, String t) {
    int i = s.length() - 1; // s's index
    int j = t.length() - 1; // t's index

    while (true) {
      // Delete chars of s if needed
      int back = 0;
      while (i >= 0 && (s.charAt(i) == '#' || back > 0)) {
        back += s.charAt(i) == '#' ? 1 : -1;
        --i;
      }
      // Delete chars of t if needed
      back = 0;
      while (j >= 0 && (t.charAt(j) == '#' || back > 0)) {
        back += t.charAt(j) == '#' ? 1 : -1;
        --j;
      }
      if (i >= 0 && j >= 0 && s.charAt(i) == t.charAt(j)) {
        --i;
        --j;
      } else {
        break;
      }
    }

    return i == -1 && j == -1;
  }
}
