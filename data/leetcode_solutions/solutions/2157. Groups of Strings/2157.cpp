class UnionFind {
 public:
  UnionFind(int n) : count(n), id(n), sz(n, 1) {
    iota(begin(id), end(id), 0);
  }

  void unionBySize(int u, int v) {
    const int i = find(u);
    const int j = find(v);
    if (i == j)
      return;
    if (sz[i] < sz[j]) {
      sz[j] += sz[i];
      id[i] = j;
    } else {
      sz[i] += sz[j];
      id[j] = i;
    }
    --count;
  }

  int getCount() const {
    return count;
  }

  int getMaxSize() const {
    return *max_element(begin(sz), end(sz));
  }

 private:
  int count;
  vector<int> id;
  vector<int> sz;

  int find(int u) {
    return id[u] == u ? u : id[u] = find(id[u]);
  }
};

class Solution {
 public:
  vector<int> groupStrings(vector<string>& words) {
    UnionFind uf(words.size());
    unordered_map<int, int> maskToIndex;
    unordered_map<int, int> deletedMaskToIndex;

    for (int i = 0; i < words.size(); ++i) {
      const int mask = getMask(words[i]);
      for (int j = 0; j < 26; ++j)
        if (mask >> j & 1) {
          // Going to delete this bit
          const int m = mask ^ 1 << j;
          if (maskToIndex.count(m))
            uf.unionBySize(i, maskToIndex[m]);
          if (deletedMaskToIndex.count(m))
            uf.unionBySize(i, deletedMaskToIndex[m]);
          else
            deletedMaskToIndex[m] = i;
        } else {
          // Going to add this bit
          const int m = mask | 1 << j;
          if (maskToIndex.count(m))
            uf.unionBySize(i, maskToIndex[m]);
        }
      maskToIndex[mask] = i;
    }

    return {uf.getCount(), uf.getMaxSize()};
  }

 private:
  int getMask(const string& s) {
    int mask = 0;
    for (const char c : s)
      mask |= 1 << c - 'a';
    return mask;
  }
};
