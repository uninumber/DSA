from typing import List

def twoSums(self, nums: List[int], target: int) -> List[int]:

    values = {}

    for idx, value in enumerate(nums):
        if value in values:
            return [values[target-value], idx]
        else:
            values[value] = idx
