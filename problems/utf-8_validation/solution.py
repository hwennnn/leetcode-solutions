def is_k_bytes_long(data, index, k):
    if k == 1:
        k = 0
    return data[index] >> (7 - k) == ((1 << k) - 1) << 1 and all(
        index2 < len(data)
        and data[index2] >> 6 == 0b10
        for index2 in range(index + 1, index + k)
    )
        
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        index = 0
        while index < len(data):
            for k in range(1, 5):
                if is_k_bytes_long(data, index, k):
                    index += k
                    break
            else:
                return False
        return True