"""
You are given an integer `num`. You know that Danny Mittal will sneakily **remap** one of the `10` possible digits (`0` to `9`) to another digit.

Return *the difference between the maximum and minimum**values Danny can make by remapping **exactly** **one** digit* *in* `num`.

**Notes:**

* When Danny remaps a digit d1 to another digit d2, Danny replaces all occurrences of `d1` in `num` with `d2`.
* Danny can remap a digit to itself, in which case `num` does not change.
* Danny can remap different digits for obtaining minimum and maximum values respectively.
* The resulting number after remapping can contain leading zeroes.
* We mentioned "Danny Mittal" to congratulate him on being in the top 10 in Weekly Contest 326.
"""
class Solution:
    def minMaxDifference(self, num: int) -> int:
        $$$