class Solution:
	def threeEqualParts(self, A: List[int]) -> List[int]:

		onesCountToIndex = {}
		count = 0
		for i, a in enumerate(A):
			if a != 0:
				count += 1
				onesCountToIndex[count] = i
		
		if count % 3 != 0:
			return [-1, -1]
		
		if count == 0:
			return [0, len(A)-1]
		
		numOnesPerPart = count // 3
		
		left = onesCountToIndex[1]
		mid = onesCountToIndex[1 + numOnesPerPart]
		right = onesCountToIndex[1 + numOnesPerPart*2]
		
		while left < mid < right < len(A) and A[left] == A[mid] == A[right]:
			left += 1
			mid += 1
			right += 1
		if right == len(A):
			return [left-1, mid]
		return [-1, -1]