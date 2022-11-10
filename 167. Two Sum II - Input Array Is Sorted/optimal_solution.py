class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        storage = {}
        storage[numbers[0]] = 0
        for ii in range(1, len(numbers)):
            if target - numbers[ii] in storage:
                return [storage[target - numbers[ii]] + 1, ii + 1]
            else:
                storage[numbers[ii]] = ii
        return []
