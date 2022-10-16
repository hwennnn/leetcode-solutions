class BinaryIndexedTree:
    def __init__(self, size):
        self._size = size + 1
        self._data = [0] * self._size

    @staticmethod
    def from_list(nums):
        tree = BinaryIndexedTree(len(nums))
        for index, num in enumerate(nums):
            tree.update(index, num)
        return tree
    
    def update(self, index, value):
        index += 1
        while index < self._size:
            self._data[index] += value
            index += index & -index
    
    def query(self, index):
        index += 1
        result = 0
        while index > 0:
            result += self._data[index]
            index -= index & -index
        return result
    
    def range_sum(self, left, right):
        return self.query(right) - self.query(left - 1)
    
class NumArray:
    def __init__(self, nums: List[int]):
        self._tree = BinaryIndexedTree.from_list(nums)
        self._nums = nums

    def update(self, index: int, val: int) -> None:
        self._tree.update(index, val - self._nums[index])
        self._nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self._tree.range_sum(left, right)