"""
There are `n` different online courses numbered from `1` to `n`. You are given
an array `courses` where `courses[i] = [durationi, lastDayi]` indicate that
the `ith` course should be taken **continuously** for `durationi` days and
must be finished before or on `lastDayi`.

You will start on the `1st` day and you cannot take two or more courses
simultaneously.

Return _the maximum number of courses that you can take_.
"""
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        $$$
