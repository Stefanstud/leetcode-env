class Solution:

    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        arr = row
        patner = defaultdict(int)  # Stores the patner

        # Populate who is patner
        for i in range(0, n - 1, 2):
            patner[i] = i + 1
            patner[i + 1] = i
        ans = 0
        # Traverse the array and swap if not with his/her patner
        for i in range(0, n - 2, 2):
            if not patner[arr[i]] == arr[i + 1]:
                ans += 1
                temp = arr.index(patner[arr[i]])
                arr[i + 1], arr[temp] = arr[temp], arr[i + 1]
        return ans
