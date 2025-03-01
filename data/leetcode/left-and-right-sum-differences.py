"""
Given a **0-indexed** integer array `nums`, find a **0-indexed** integer array `answer` where:

* `answer.length == nums.length`.
* `answer[i] = |leftSum[i] - rightSum[i]|`.

Where:

* `leftSum[i]` is the sum of elements to the left of the index `i` in the array `nums`. If there is no such element, `leftSum[i] = 0`.
* `rightSum[i]` is the sum of elements to the right of the index `i` in the array `nums`. If there is no such element, `rightSum[i] = 0`.

Return *the array* `answer`.
"""
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        $$$