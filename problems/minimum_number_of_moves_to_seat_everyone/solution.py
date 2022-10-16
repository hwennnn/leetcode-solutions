class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(s1 - s2) for s1, s2 in zip(sorted(seats), sorted(students)))