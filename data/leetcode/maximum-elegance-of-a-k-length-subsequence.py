"""
You are given a **0-indexed** 2D integer array `items` of length `n` and an integer `k`.

`items[i] = [profiti, categoryi]`, where `profiti` and `categoryi` denote the profit and category of the `ith` item respectively.

Let's define the **elegance** of a **subsequence** of `items` as `total_profit + distinct_categories2`, where `total_profit` is the sum of all profits in the subsequence, and `distinct_categories` is the number of **distinct** categories from all the categories in the selected subsequence.

Your task is to find the **maximum elegance** from all subsequences of size `k` in `items`.

Return *an integer denoting the maximum elegance of a subsequence of* `items` *with size exactly* `k`.

**Note:** A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order.
"""
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        $$$