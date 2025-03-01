"""
Given an integer array `nums` sorted in **non-decreasing order** , remove the
duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm)
such that each unique element appears only **once**. The **relative order** of
the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the **first part** of the array
`nums`. More formally, if there are `k` elements after removing the
duplicates, then the first `k` elements of `nums` should hold the final
result. It does not matter what you leave beyond the first `k` elements.

Return `k` _after placing the final result in the first_`k` _slots of_`nums`.

Do **not** allocate extra space for another array. You must do this by
**modifying the input array[in-place](https://en.wikipedia.org/wiki/In-
place_algorithm)** with O(1) extra memory.

**Custom Judge:**

The judge will test your solution with the following code:

    
    
    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length
    
    int k = removeDuplicates(nums); // Calls your implementation
    
    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
    

If all assertions pass, then your solution will be **accepted**.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        $$$
