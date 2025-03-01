"""
There are `n` workers. You are given two integer arrays `quality` and `wage`
where `quality[i]` is the quality of the `ith` worker and `wage[i]` is the
minimum wage expectation for the `ith` worker.

We want to hire exactly `k` workers to form a paid group. To hire a group of
`k` workers, we must pay them according to the following rules:

  1. Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
  2. Every worker in the paid group must be paid at least their minimum wage expectation.

Given the integer `k`, return _the least amount of money needed to form a paid
group satisfying the above conditions_. Answers within `10-5` of the actual
answer will be accepted.
"""
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        $$$
