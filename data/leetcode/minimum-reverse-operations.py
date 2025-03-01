"""
You are given an integer `n` and an integer `p` in the range `[0, n - 1]`. Representing a **0-indexed** array `arr` of length `n` where all positions are set to `0`'s, except position `p` which is set to `1`.

You are also given an integer array `banned` containing some positions from the array. For the **i****th** position in `banned`, `arr[banned[i]] = 0`, and `banned[i] != p`.

You can perform **multiple** operations on `arr`. In an operation, you can choose a **subarray** with size `k` and **reverse** the subarray. However, the `1` in `arr` should never go to any of the positions in `banned`. In other words, after each operation `arr[banned[i]]` **remains** `0`.

*Return an array* `ans` *where* *for each* `i` *from* `[0, n - 1]`, `ans[i]` *is the **minimum** number of reverse operations needed to bring the* `1` *to position* `i` *in arr*, *or* `-1` *if it is impossible*.

* A **subarray** is a contiguous **non-empty** sequence of elements within an array.
* The values of `ans[i]` are independent for all `i`'s.
* The **reverse** of an array is an array containing the values in **reverse order**.
"""
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        $$$