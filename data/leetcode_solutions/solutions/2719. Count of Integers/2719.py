class Solution:
    M = 1000000007

    def add(self, x, y) -> int:
        x += y
        if x >= self.M:
            x -= self.M
        return x


    def sub(self, x, y) -> int:
        x -= y
        if x < 0:
            x += self.M
        return x


    def count_strings(self, s, min_sum, max_sum) -> int:
        n = len(s)
        m = min(max_sum, 9 * n)
        dp = [[[0 for _ in range(m + 1)] for _ in range(2)] for _ in range(2)]
        dp[0][0][0] = 1
        last = 0
        for i in range(n):
            p = i * 9
            now = last ^ 1
            dp[now] = [[0 for _ in range(m + 1)] for _ in range(2)]
            for j in range(2):
                for k in range(min(m, p) + 1):
                    if dp[last][j][k] == 0:
                        continue
                    for c in range(ord('9') if j else ord(s[i]), ord('0') - 1, -1):
                        q = k + c - ord('0')
                        if q <= m:
                            dp[now][j or (c < ord(s[i]))][q] = self.add(
                                dp[now][j or (c < ord(s[i]))][q], dp[last][j][k]
                            )
            last ^= 1
        r = 0
        for i in range(2):
            for j in range(min_sum, m + 1):
                r = self.add(r, dp[last][i][j])
        return r

    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        s = sum(int(c) for c in num1)
        r = self.count_strings(num2, min_sum, max_sum)
        r = self.sub(r, self.count_strings(num1, min_sum, max_sum))
        if min_sum <= s <= max_sum:
            r = self.add(r, 1)
        return r